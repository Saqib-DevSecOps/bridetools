# Generated by Django 3.2.19 on 2023-06-20 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_backgroundimage_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='backgroundimage',
            name='about_background',
            field=models.ImageField(blank=True, null=True, upload_to='background/'),
        ),
    ]
