# Generated by Django 3.2.6 on 2022-09-05 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AutoUser', '0003_autouser_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autouser',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]