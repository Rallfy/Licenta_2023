# Generated by Django 4.1.7 on 2023-06-11 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_bookproduct_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='id',
            field=models.AutoField(default='number', editable=False, primary_key=True, serialize=False),
        ),
    ]
