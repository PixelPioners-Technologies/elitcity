# Generated by Django 4.2.7 on 2024-01-22 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complex', '0004_ground_names_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='ground_names',
            name='rank',
            field=models.CharField(choices=[('A', 'Rank A'), ('B', 'Rank B'), ('C', 'Rank C'), ('D', 'Rank D'), ('E', 'Rank E')], default='E', max_length=1),
        ),
    ]