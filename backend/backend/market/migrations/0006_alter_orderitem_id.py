# Generated by Django 4.1.7 on 2023-06-11 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0005_alter_orderitem_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
    ]
