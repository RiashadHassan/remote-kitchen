# Generated by Django 5.1.1 on 2024-09-07 10:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addressio', '0002_initial'),
        ('core', '0003_organization_media_files_organizationmember_member_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='addressconnector',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.organization'),
        ),
    ]
