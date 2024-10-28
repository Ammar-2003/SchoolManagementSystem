# Generated by Django 5.1.1 on 2024-10-18 08:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PayStructure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('annual_increment', models.IntegerField()),
                ('basic_pay', models.IntegerField()),
                ('conveyance_allowance', models.IntegerField()),
                ('hra', models.IntegerField()),
                ('medical_allowance', models.IntegerField()),
                ('employee_designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employeedesignation')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
