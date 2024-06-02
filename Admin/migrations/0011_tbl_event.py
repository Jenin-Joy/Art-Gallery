# Generated by Django 5.0.6 on 2024-05-29 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0010_delete_tbl_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=30)),
                ('event_start_date', models.DateField()),
                ('event_end_date', models.DateField()),
                ('event_details', models.CharField(max_length=30)),
                ('event_seat', models.CharField(max_length=30)),
                ('event_image', models.FileField(upload_to='Assets/EventPhoto/')),
            ],
        ),
    ]