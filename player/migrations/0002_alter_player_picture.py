# Generated by Django 4.0 on 2022-01-04 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Photo'),
        ),
    ]
