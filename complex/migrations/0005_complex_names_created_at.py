# Generated by Django 4.2.7 on 2024-01-08 15:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('complex', '0004_alter_complex_names_full_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='complex_names',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]