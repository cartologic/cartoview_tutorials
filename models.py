from django.db import models
from datetime import datetime
from django.conf import settings
from .validators import validate_file
from django.db.models.signals import post_save
from django.dispatch import receiver
import os
from django.utils.safestring import mark_safe


def get_tutorial_path(instance, filename):
    today = datetime.now()
    date_as_path = today.strftime("%Y/%m/%d")
    return '/'.join(['tutorials', date_as_path, filename])


class Tutorial(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    description = models.TextField(null=True, blank=True)
    file = models.FileField(
        upload_to=get_tutorial_path, null=False, blank=False,
        validators=[validate_file])
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    url = models.URLField(null=True, blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='tutorials',
        null=True, blank=True)

    def get_html(self):
        filename = self.file.name
        ext = os.path.splitext(filename)[1][1:].lower()
        file_url = self.file.url
        dom = None
        if ext == 'pdf':
            dom = '''
            <object data="{}" class="tutorial-img" type="application/pdf">
                alt : <a href="{}">{}</a>
            </object>
            '''.format(file_url, file_url, filename)
            # dom = '<embed src="{}" class="tutorial-img" />'.format(
            #     self.file.url)
        elif ext == "mp4":
            dom = """
            <video class="tutorial-img" controls>
                <source src="{}" type="video/mp4">
                Your browser does not support the video tag.
            </video>
            """.format(file_url)
        else:
            dom = '<img src="{}" class="tutorial-img" />'.format(file_url)
        return mark_safe(dom)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


# @receiver(post_save, sender=Tutorial)
# def update_file_type(sender, instance, **kwargs):
#     filename = instance.file.name
#     is_image = check_image(filename)
#     if instance.is_image != is_image:
#         instance.is_image = is_image
#         instance.save()
