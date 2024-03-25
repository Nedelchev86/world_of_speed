from django.core.exceptions import ValidationError


def username_letter_validator(value):
    for char in value:
        if not char.isalnum() and char != "_":
            raise ValidationError("Username must contain only letters, digits, and underscores!")
