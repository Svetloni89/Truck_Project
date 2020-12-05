from django.core.exceptions import ValidationError


def validator_phone_only_numeric(phone):
    if not str(phone).isdigit():
        raise ValidationError('The phone number should contain only numeric')
