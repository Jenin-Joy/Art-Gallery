# Generated by Django 5.0.6 on 2024-05-30 10:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0008_remove_tbl_artist_artist_gender'),
        ('User', '0010_remove_tbl_tickets_booking_delete_tbl_ticket_booking_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_ticket_booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateField(auto_now_add=True)),
                ('booking_status', models.IntegerField(default=0)),
                ('booking_totalamount', models.CharField(max_length=50, null=True)),
                ('booking_time', models.TimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_no', models.IntegerField()),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.tbl_ticket_booking')),
            ],
        ),
    ]
