# Generated by Django 3.2.7 on 2021-09-13 16:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0008_issue_is_restricted'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssueAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.PositiveSmallIntegerField(choices=[(1, 'Accepted'), (2, 'Rejected'), (3, 'Pending Verification')], default=3, verbose_name='State')),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.issue')),
                ('requester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
