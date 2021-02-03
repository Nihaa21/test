# Generated by Django 3.1.1 on 2020-11-06 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTwo', '0010_auto_20201103_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='amc_amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='amc_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='amc_expiry_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='chatbot_amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='chatbot_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='chatbot_last_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='chatbot_type',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='credits_purchased',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='project_details',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='project_update',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='sll_account',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='sll_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='sll_expiry_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='sll_type',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='updated_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='expiry_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='purchase_date',
            field=models.DateField(null=True),
        ),
    ]
