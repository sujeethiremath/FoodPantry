# Generated by Django 2.2.5 on 2020-04-29 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0005_inventory_donor'),
    ]

    operations = [
        migrations.CreateModel(
            name='checkout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=9)),
                ('checkout_date', models.DateField()),
                ('item_name', models.CharField(max_length=50)),
                ('quantity', models.PositiveIntegerField()),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory', to='inventory.inventory')),
            ],
        ),
    ]
