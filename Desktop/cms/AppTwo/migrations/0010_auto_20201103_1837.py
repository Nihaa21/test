# Generated by Django 3.1.1 on 2020-11-03 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTwo', '0009_auto_20201022_0603'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='hosting_account',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='hosting_amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='hosting_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='hosting_expiry_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='hosting_pass',
            field=models.CharField(max_length=10, null=True),
        ),
    ]