# Generated by Django 5.0.4 on 2024-05-15 20:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_customer_state_delete_addresses'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderplaced',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.customer'),
        ),
    ]