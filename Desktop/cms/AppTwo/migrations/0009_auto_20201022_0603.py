# Generated by Django 3.1.1 on 2020-10-22 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTwo', '0008_auto_20201019_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='purchase_date',
            field=models.DateField(),
        ),
    ]
