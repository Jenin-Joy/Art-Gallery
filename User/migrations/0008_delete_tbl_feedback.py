# Generated by Django 5.0.6 on 2024-05-16 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0007_tbl_booking_tbl_complaint_tbl_feedback_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_feedback',
        ),
    ]