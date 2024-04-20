# Generated by Django 5.0.4 on 2024-04-20 04:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Employee', '0015_alter_employee_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='App_Employee.department'),
        ),
    ]
