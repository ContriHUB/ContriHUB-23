# Generated by Django 3.2.7 on 2021-09-27 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0022_alter_pullrequest_pr_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='domain',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Domain'),
        ),
    ]
