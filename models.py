from django.db import models
from datetime import datetime
from django.conf import settings
from .validators import validate_file


def get_tutorial_path(instance, filename):
    today = datetime.now()
    date_as_path = today.strftime("%Y/%m/%d")
    return '/'.join(['tutorials', date_as_path, filename])


class Tutorial(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    description = models.TextField(null=True)
    file = models.FileField(
        upload_to=get_tutorial_path, null=False, blank=False,
        validators=[validate_file])
    is_image = models.BooleanField(default=True, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='tutorials',
        null=True, blank=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
