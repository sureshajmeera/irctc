# Generated by Django 5.0.3 on 2024-08-04 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irctc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IRCTCADMIN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Train_name', models.CharField(max_length=100)),
                ('From_Station', models.CharField(max_length=100)),
                ('To_station', models.CharField(max_length=100)),
                ('seat_Capacity', models.IntegerField()),
                ('Depatured_Time_And_Date', models.DateTimeField()),
                ('Arrival_Time_And_Date', models.DateTimeField()),
            ],
        ),
    ]
