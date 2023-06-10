# Generated by Django 4.0.10 on 2023-06-10 07:59

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_alter_event_host'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', tinymce.models.HTMLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='_ no name _', max_length=255)),
                ('address', models.CharField(default='_ no address provided _', max_length=1000)),
                ('phone', models.CharField(default='+000000000000', max_length=15)),
                ('email', models.EmailField(default='noname@domain.com', max_length=255)),
                ('privacy_content', tinymce.models.HTMLField(default='*')),
                ('terms_content', tinymce.models.HTMLField(default='*')),
                ('disclaimer_content', tinymce.models.HTMLField(default='*')),
                ('contact_content', tinymce.models.HTMLField(default='*')),
            ],
            options={
                'verbose_name_plural': 'Site',
            },
        ),
    ]
