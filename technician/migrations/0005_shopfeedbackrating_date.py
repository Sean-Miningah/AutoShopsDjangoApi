# Generated by Django 3.2.6 on 2022-09-05 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technician', '0004_alter_techniciandetails_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopfeedbackrating',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
