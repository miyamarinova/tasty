from django.db import models

from tasty.accounts.models import Profile

MAX_LENGTH_CHAR_CUISINE_TYPE = 7
CUISINE_CHOICES = [
    ('French', 'French'),
    ('Chinese', 'Chinese'),
    ('Italian', 'Italian'),
    ('Balkan', 'Balkan'),
    ('Other', 'Other'),
]


# Create your models here.
class Recipe(models.Model):
    title = models.CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=30
    )

    cuisine_type = models.CharField(
        max_length=MAX_LENGTH_CHAR_CUISINE_TYPE,
        choices=CUISINE_CHOICES
    )

    ingredients = models.TextField(
        null=False,
        blank=False,
        help_text="Ingredients must be separated by a comma and space."
    )

    instructions = models.TextField(
        null=False,
        blank=False
    )

    cooking_time = models.PositiveIntegerField(
        null=False,
        blank=False,
        help_text='Provide the cooking time in minutes.'
    )

    image_url = models.URLField(
        null=True,
        blank=True
    )

    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='recipes',
        editable=False
    )

