from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from world_of_speed.profiles.validators import username_letter_validator


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(3),
            username_letter_validator
        ],
        error_messages={
            'min_length': 'Username must be at least 3 chars long!'
        },
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        validators=[MinValueValidator(21)],
        null=False,
        blank=False,
        help_text="Age requirement: 21 years and above."
    )

    password = models.CharField(
        max_length=20,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=25,
    )

    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=25,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
