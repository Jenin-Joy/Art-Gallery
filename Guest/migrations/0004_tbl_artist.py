# Generated by Django 5.0.3 on 2024-03-24 17:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0006_tbl_subcategory'),
        ('Guest', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(max_length=50)),
                ('artist_gender', models.CharField(max_length=50)),
                ('artist_contact', models.CharField(max_length=50)),
                ('artist_email', models.CharField(max_length=50)),
                ('artist_address', models.CharField(max_length=500)),
                ('artist_about', models.CharField(max_length=500)),
                ('artist_password', models.CharField(max_length=50)),
                ('artist_photo', models.FileField(upload_to='Assets/ArtistPhoto/')),
                ('artist_proof', models.FileField(upload_to='Assets/ArtistProof/')),
                ('artist_status', models.IntegerField(default='0')),
                ('artist_doj', models.DateField(auto_now_add=True)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_place')),
            ],
        ),
    ]
