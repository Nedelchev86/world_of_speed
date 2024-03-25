from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from world_of_speed.cars.validators import validate_year_range
from world_of_speed.profiles.models import Profile


class Car(models.Model):
    CAR_TYPES = (
        ("Rally", "Rally"),
        ("Open-wheel", "Open-wheel"),
        ("Kart", "Kart"),
        ("Drag", "Drag"),
        ("Other", "Other"),
    )

    type = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        choices=CAR_TYPES
    )

    model = models.CharField(
        max_length=15,
        validators=[MinLengthValidator(1)],
        null=False,
        blank=False,
    )

    year = models.IntegerField(
        null=False,
        blank=False,
        validators=[validate_year_range]
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        unique=True,
        error_messages={
            'unique': 'This image URL is already in use! Provide a new one.'},
        verbose_name="Image URL",
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=[MinValueValidator(1.0)]
    )

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )