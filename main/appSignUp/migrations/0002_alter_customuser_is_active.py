# Generated by Django 4.1.11 on 2023-10-02 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appSignUp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default='True'),
        ),
    ]
