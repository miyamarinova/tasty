# Generated by Django 5.0.4 on 2024-04-17 10:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True)),
                ('cuisine_type', models.CharField(choices=[('F', 'French'), ('C', 'Chinese'), ('I', 'Italian'), ('B', 'Balkan'), ('O', 'Other')], max_length=7)),
                ('ingredients', models.TextField(help_text='Ingredients must be separated by a comma and space.')),
                ('instructions', models.TextField()),
                ('cooking_time', models.PositiveIntegerField(help_text='Provide the cooking time in minutes.')),
                ('image_url', models.URLField(blank=True, null=True)),
                ('author', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to='accounts.profile')),
            ],
        ),
    ]
