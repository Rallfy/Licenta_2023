# Generated by Django 4.1.7 on 2023-06-21 20:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0019_alter_bookproduct_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookproduct',
            name='category',
            field=models.CharField(blank=True, default=django.utils.timezone.now, max_length=200, null=True),
        ),
    ]
