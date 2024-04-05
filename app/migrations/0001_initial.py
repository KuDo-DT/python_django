# Generated by Django 5.0.3 on 2024-03-25 03:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField()),
                ('digital', models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('User', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Oder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_oder', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False, null=True)),
                ('transaction_id', models.CharField(max_length=200, null=True)),
                ('Customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Oder_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('Oder', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.oder')),
                ('Product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.product')),
            ],
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200, null=True)),
                ('city', models.CharField(max_length=200, null=True)),
                ('State', models.CharField(max_length=200, null=True)),
                ('mobile', models.CharField(max_length=200, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('Customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.customer')),
                ('Oder', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.oder')),
            ],
        ),
    ]
