# Generated by Django 4.0 on 2021-12-25 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0007_alter_profile_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Nom du club')),
                ('city', models.CharField(max_length=128, verbose_name='Ville')),
                ('province', models.CharField(max_length=128, verbose_name='Département')),
                ('level', models.CharField(max_length=128, verbose_name='Niveau')),
                ('picture', models.ImageField(null=True, upload_to='', verbose_name='Photo')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.profile')),
            ],
        ),
    ]