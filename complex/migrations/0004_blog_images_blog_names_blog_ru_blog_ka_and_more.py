# Generated by Django 4.2.1 on 2024-01-19 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('complex', '0003_alter_ground_ka_ground_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='blog_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Blog_Names',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('picture_link', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog_RU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_name_ru', models.CharField(max_length=100, null=True)),
                ('blog_images', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='complex.blog_images')),
                ('internal_blog_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complex.blog_names')),
            ],
        ),
        migrations.CreateModel(
            name='Blog_KA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_name_ka', models.CharField(max_length=100, null=True)),
                ('blog_images', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='complex.blog_images')),
                ('internal_blog_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complex.blog_names')),
            ],
        ),
        migrations.AddField(
            model_name='blog_images',
            name='internal_blog_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complex.blog_names'),
        ),
        migrations.CreateModel(
            name='Blog_EN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_name_en', models.CharField(max_length=100, null=True)),
                ('blog_images', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='complex.blog_images')),
                ('internal_blog_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complex.blog_names')),
            ],
        ),
    ]