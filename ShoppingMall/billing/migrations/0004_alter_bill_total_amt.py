# Generated by Django 5.0.4 on 2024-04-06 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0003_alter_bill_total_amt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='total_amt',
            field=models.IntegerField(default=0),
        ),
    ]