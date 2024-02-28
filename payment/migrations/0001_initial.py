# Generated by Django 5.0 on 2024-02-28 19:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('group', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateTimeField(auto_now_add=True, verbose_name='дата платежа')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='сумма оплаты')),
                ('payment_method', models.CharField(choices=[('cash', 'наличные'), ('bank_transfer', 'перевод на счет')], max_length=20, verbose_name='способ оплаты')),
                ('lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payment', to='group.lesson', verbose_name='урок')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payment', to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
                ('well', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payment', to='group.well', verbose_name='курс')),
            ],
            options={
                'verbose_name': 'платеж',
                'verbose_name_plural': 'платежи',
            },
        ),
    ]