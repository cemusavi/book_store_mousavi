# Generated by Django 3.2.6 on 2021-08-14 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='percent',
            name='percent',
            field=models.PositiveIntegerField(verbose_name='Percent Discount'),
        ),
    ]