# Generated by Django 3.1.1 on 2020-11-06 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTwo', '0011_auto_20201106_0703'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='sll_amount',
            field=models.IntegerField(null=True),
        ),
    ]
