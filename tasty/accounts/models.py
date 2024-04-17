from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
MAX_LENGTH_NAME = 30

class Profile(models.Model):
    nickname = models.CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=MAX_LENGTH_NAME
    )

    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LENGTH_NAME,

    )

    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LENGTH_NAME
    )

    chef = models.BooleanField(
        null=False,
        default=False
    )

    bio = models.TextField(
        null=True,
        blank=True
    )


    def clean(self):
        if self.first_name and not self.first_name[0].isupper():
            raise ValidationError("Name must start with a capital letter!")
        if self.last_name and not self.last_name[0].isupper():
            raise ValidationError("Name must start with a capital letter!")

