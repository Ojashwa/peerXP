# Generated by Django 3.1.2 on 2020-10-24 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Support', '0003_userlogin_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlogin',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
