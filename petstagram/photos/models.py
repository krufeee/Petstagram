from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.core.model_mixins import StrFromFieldsMixin
from petstagram.pets.models import Pet
from petstagram.photos.validators import validate_image_less_than_5mb


class Photo(StrFromFieldsMixin, models.Model):
    str_fields = ('pk', 'photo', 'location')
    MIN_DESCRIPTION_LEN = 10
    MAX_DESCRIPTION_LEN = 300

    MAX_LOCATION_LEN = 30

    photo = models.ImageField(
        upload_to='mediafiles/pet_photos',
        null=False,
        blank=True,
        validators=(validate_image_less_than_5mb,),
    )

    description = models.CharField(
        null=True,
        blank=True,
        max_length=MAX_DESCRIPTION_LEN,
        validators=(
            MinLengthValidator(MIN_DESCRIPTION_LEN),

        )

    )

    location = models.CharField(
        null=True,
        blank=True,
        max_length=MAX_LOCATION_LEN,
    )

    publication_date = models.DateField(
        blank=True,
        null=False,
        auto_now=True,
    )

    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
    )

