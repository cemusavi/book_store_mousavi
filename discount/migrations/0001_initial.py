# Generated by Django 3.2.6 on 2021-08-14 11:11

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('expiration_date', models.DateTimeField(verbose_name='Expiration Date')),
                ('cash', models.PositiveIntegerField(verbose_name='Cash Discount')),
            ],
            options={
                'verbose_name': 'Cash Discount',
                'verbose_name_plural': 'Cash Discounts',
            },
        ),
        migrations.CreateModel(
            name='CashCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('code', models.CharField(max_length=30, verbose_name='Code Discount')),
                ('expiration_date', models.DateTimeField(verbose_name='Expiration Date')),
                ('cash', models.PositiveIntegerField(verbose_name='Cash Code Discount')),
            ],
            options={
                'verbose_name': 'Cash Code Discount',
                'verbose_name_plural': 'Cash Code Discounts',
            },
        ),
        migrations.CreateModel(
            name='Percent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('expiration_date', models.DateTimeField(verbose_name='Expiration Date')),
                ('percent', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(limit_value=99), django.core.validators.MinValueValidator(limit_value=1)], verbose_name='Percent Discount')),
            ],
            options={
                'verbose_name': 'Percent Discount',
                'verbose_name_plural': 'Percent Discounts',
            },
        ),
        migrations.CreateModel(
            name='PercentCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('code', models.CharField(max_length=30, verbose_name='Code Discount')),
                ('expiration_date', models.DateTimeField(verbose_name='Expiration Date')),
                ('percent', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(limit_value=99), django.core.validators.MinValueValidator(limit_value=1)], verbose_name='Percent Code Discount')),
            ],
            options={
                'verbose_name': 'Percent Code Discount',
                'verbose_name_plural': 'Percent Code Discounts',
            },
        ),
        migrations.CreateModel(
            name='SpecificPercent',
            fields=[
                ('percent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='discount.percent')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specific_percent', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Specific Percent Discount',
                'verbose_name_plural': 'Specific Percent Discounts',
            },
            bases=('discount.percent',),
        ),
        migrations.CreateModel(
            name='SpecificCash',
            fields=[
                ('cash_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='discount.cash')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specific_cash', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Specific Cash Discount',
                'verbose_name_plural': 'Specific Cash Discounts',
            },
            bases=('discount.cash',),
        ),
    ]
