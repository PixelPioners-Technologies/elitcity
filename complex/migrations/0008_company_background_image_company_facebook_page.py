# Generated by Django 4.2.7 on 2023-11-15 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complex', '0007_company_complex_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to='company_background_images/'),
        ),
        migrations.AddField(
            model_name='company',
            name='facebook_page',
            field=models.URLField(blank=True, null=True),
        ),
    ]