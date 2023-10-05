# Generated by Django 3.2.7 on 2021-09-13 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0005_auto_20210913_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='course',
            field=models.PositiveSmallIntegerField(choices=[(1, 'B.Tech'), (2, 'M.C.A'), (3, 'M.Tech'), (4, 'M.Sc'), (5, 'P.H.D')], default=1, verbose_name='Course'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='current_year',
            field=models.PositiveSmallIntegerField(choices=[(1, 'First'), (2, 'Second'), (3, 'Third'), (4, 'Final')], default=1, verbose_name='Current Year'),
        ),
    ]
