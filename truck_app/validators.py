from django.core.exceptions import ValidationError


def validator_comment_end(comment):
    if not comment.endswith(('.', '!', '?',)):
        raise ValidationError('The comment should ends whit ( . or ! or ? )')


def validator_price_is_digit(price):
    if not str(price).isdigit():
        raise ValidationError('The price should be integer!')
