# Generated by Django 5.0.4 on 2024-04-27 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Employee', '0021_alter_employee_join_department_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compensation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='compensations',
            field=models.ManyToManyField(blank=True, null=True, to='App_Employee.compensation'),
        ),
    ]
