# Generated by Django 5.1.1 on 2024-10-22 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0004_alter_academicinfo_admission_class_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admission',
            name='admission_by',
        ),
        migrations.RemoveField(
            model_name='admission',
            name='admission_confirmation_date',
        ),
        migrations.RemoveField(
            model_name='admission',
            name='admission_no',
        ),
        migrations.RemoveField(
            model_name='admission',
            name='admission_type',
        ),
    ]
