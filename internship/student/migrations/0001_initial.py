# Generated by Django 3.2 on 2025-01-05 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studentRegister_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('register_no', models.IntegerField(unique=True)),
                ('department', models.CharField(max_length=50)),
            ],
        ),
    ]
