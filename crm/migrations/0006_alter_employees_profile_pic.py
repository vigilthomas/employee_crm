# Generated by Django 4.2.2 on 2023-11-14 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_alter_employees_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='crm/static/emp_img'),
        ),
    ]
