# Generated by Django 4.1.1 on 2022-09-23 23:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fotos', '0002_alter_foto_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='foto',
            name='owner',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
