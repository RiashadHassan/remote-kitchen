# Generated by Django 5.1.1 on 2024-09-07 10:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('addressio', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='addressconnector',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='address',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='addressio.district'),
        ),
        migrations.AddField(
            model_name='district',
            name='division',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='addressio.division'),
        ),
        migrations.AddField(
            model_name='address',
            name='division',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='addressio.division'),
        ),
        migrations.AddField(
            model_name='postoffice',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='addressio.district'),
        ),
        migrations.AddField(
            model_name='postoffice',
            name='division',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='addressio.division'),
        ),
        migrations.AddField(
            model_name='address',
            name='post_office',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='addressio.postoffice'),
        ),
        migrations.AddField(
            model_name='upazila',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addressio.district'),
        ),
        migrations.AddField(
            model_name='upazila',
            name='division',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addressio.division'),
        ),
        migrations.AddField(
            model_name='postoffice',
            name='upazila',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='addressio.upazila'),
        ),
        migrations.AddField(
            model_name='address',
            name='upazila',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='addressio.upazila'),
        ),
        migrations.AlterUniqueTogether(
            name='addressconnector',
            unique_together={('address', 'user')},
        ),
        migrations.AlterUniqueTogether(
            name='upazila',
            unique_together={('name', 'district', 'division')},
        ),
    ]
