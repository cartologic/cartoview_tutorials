from django.core.exceptions import ValidationError
import os

ALLOWED_TYPES = ['jpg', 'jpeg', 'png', 'gif', 'mp4','pdf']


def validate_file(value):
    extension = os.path.splitext(value.name)[1][1:].lower()
    if extension not in ALLOWED_TYPES:
        raise ValidationError(u'Unsupported file type.')
