# Generated by Django 5.0.7 on 2024-08-18 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hookahs', '0015_remove_order_address_remove_order_number_of_people_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='number_of_people',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
