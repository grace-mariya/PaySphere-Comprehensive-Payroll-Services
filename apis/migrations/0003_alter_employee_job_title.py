# Generated by Django 5.0.4 on 2024-11-14 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_employee_delete_employer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='job_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
