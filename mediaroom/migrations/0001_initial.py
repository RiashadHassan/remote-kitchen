# Generated by Django 5.1.1 on 2024-09-07 10:40

import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MediaRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(blank=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, height_field='height', null=True, upload_to='', width_field='width')),
                ('title', models.CharField(blank=True, max_length=500)),
                ('width', models.PositiveIntegerField(blank=True, null=True)),
                ('height', models.PositiveIntegerField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('type', models.CharField(blank=True, choices=[('IMAGE', 'Image'), ('VIDEO', 'Video'), ('ATTACHED_FILE', 'Attached File')], max_length=50, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
