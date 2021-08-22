import re

from django.core import exceptions
from django.utils.translation import ugettext_lazy as _


def phone_number_validator(value):
    pattern = r'^09[0-3][\d]{8}$'
    if re.match(pattern, value) is None:
        raise exceptions.ValidationError(
            _(f'{value} is not a valid phone number.'),
            params={'value': value}
        )
