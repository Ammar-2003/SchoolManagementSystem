# Generated by Django 5.1.1 on 2024-10-18 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('bank_account_no', models.CharField(max_length=255)),
                ('bank_address', models.CharField(max_length=255)),
                ('bank_code', models.CharField(max_length=255)),
                ('bank_contact', models.IntegerField()),
                ('bank_for_security', models.BooleanField()),
                ('bank_manager', models.CharField(max_length=255)),
                ('bank_name', models.CharField(max_length=255)),
                ('show_on_voucher', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
