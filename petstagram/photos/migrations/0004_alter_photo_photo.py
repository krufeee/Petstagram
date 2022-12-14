# Generated by Django 4.0.5 on 2022-10-22 09:47

from django.db import migrations, models
import petstagram.photos.validators


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_alter_photo_description_alter_photo_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(blank=True, upload_to='mediafiles/pet_photos', validators=[petstagram.photos.validators.validate_image_less_than_5mb]),
        ),
    ]
