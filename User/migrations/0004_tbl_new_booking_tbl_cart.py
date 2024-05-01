# Generated by Django 5.0.4 on 2024-04-29 08:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Artist', '0002_rename_artid_tbl_artistwork_artist'),
        ('Guest', '0004_tbl_artist'),
        ('User', '0003_tbl_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_new_booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateField(auto_now_add=True)),
                ('booking_status', models.IntegerField(default=0)),
                ('booking_totalamount', models.CharField(max_length=50, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_status', models.CharField(default='0', max_length=5)),
                ('cart_qty', models.CharField(max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Artist.tbl_artistwork')),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.tbl_new_booking')),
            ],
        ),
    ]
