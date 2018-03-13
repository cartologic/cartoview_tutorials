from django.core.exceptions import ValidationError
import re
import mimetypes


def validate_file(value):
    r = re.compile("(?P<type>(image|video)/[\w\d\s+-/-*]{1,6})")
    file_name = value.name
    mimetype, encoding = mimetypes.guess_type(file_name, strict=True)
    if not mimetype or not r.match(mimetype):
        raise ValidationError(u'Unsupported file type.')
