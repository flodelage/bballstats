# Generated by Django 4.0 on 2021-12-25 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_profile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(error_messages={'unique': 'Un utilisateur avec ce nom existe déjà.'}, max_length=128, unique=True, verbose_name='Utilisateur'),
        ),
    ]
