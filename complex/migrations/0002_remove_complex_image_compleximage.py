# Generated by Django 4.2.7 on 2023-11-25 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('complex', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complex',
            name='image',
        ),
        migrations.CreateModel(
            name='ComplexImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='complex_images/')),
                ('complex', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_images', to='complex.complex')),
            ],
        ),
    ]