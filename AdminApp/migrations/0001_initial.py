# Generated by Django 5.0.6 on 2024-06-20 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminModel',
            fields=[
                ('admin_id', models.AutoField(primary_key=True, serialize=False)),
                ('admin_name', models.CharField(max_length=100)),
                ('admin_mail', models.CharField(max_length=100)),
                ('admin_phone', models.CharField(max_length=100)),
                ('admin_password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentModel',
            fields=[
                ('department_id', models.AutoField(primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=100)),
            ],
        ),
    ]
