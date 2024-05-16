# Generated by Django 5.0.6 on 2024-05-16 05:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Artist', '0005_alter_tbl_artistprogram_program_image_and_more'),
        ('Guest', '0007_alter_tbl_user_user_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_artist')),
            ],
        ),
    ]