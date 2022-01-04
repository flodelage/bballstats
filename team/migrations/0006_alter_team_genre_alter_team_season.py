# Generated by Django 4.0 on 2022-01-04 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0005_alter_team_genre_alter_team_season'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='genre',
            field=models.CharField(choices=[('Femmes', 'Femmes'), ('Hommes', 'Hommes')], default='Femmes', max_length=9, verbose_name='Sexe'),
        ),
        migrations.AlterField(
            model_name='team',
            name='season',
            field=models.CharField(choices=[('2021-2022', '2021-2022'), ('2022-2023', '2022-2023'), ('2023-2024', '2023-2024')], default='2022-2023', max_length=9, verbose_name='Saison'),
        ),
    ]
