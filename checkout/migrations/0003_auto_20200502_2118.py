# Generated by Django 2.2.5 on 2020-05-03 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_remove_checkout_item_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='inventory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_in_inventory', to='inventory.inventory'),
        ),
    ]
