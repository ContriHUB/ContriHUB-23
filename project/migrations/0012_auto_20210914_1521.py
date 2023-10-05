# Generated by Django 3.2.7 on 2021-09-14 09:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0011_rename_issueassignment_issueassignmentrequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issueassignmentrequest',
            name='decided_at',
        ),
        migrations.CreateModel(
            name='ActiveIssue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_at', models.DateTimeField(blank=True, null=True, verbose_name='Decided At')),
                ('contributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.issue')),
            ],
        ),
    ]
