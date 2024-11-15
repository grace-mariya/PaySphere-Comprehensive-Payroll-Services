# Generated by Django 5.0.4 on 2024-11-14 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0003_alter_employee_job_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='hire_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
