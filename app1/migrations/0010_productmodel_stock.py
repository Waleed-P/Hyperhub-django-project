# Generated by Django 5.0.1 on 2024-02-05 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_inventorymodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='stock',
            field=models.BooleanField(default=False),
        ),
    ]
