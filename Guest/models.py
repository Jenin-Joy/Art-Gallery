from django.db import models
from Admin.models import *
# Create your models here.
class tbl_user(models.Model):
    user_name=models.CharField(max_length=50)
    user_gender=models.CharField(max_length=50)
    user_contact=models.CharField(max_length=50)
    user_email=models.CharField(max_length=50)
    user_address=models.CharField(max_length=50)
    user_password=models.CharField(max_length=50)
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    user_photo = models.FileField(upload_to='Assets/UserPhoto/')
    user_status = models.IntegerField(default="1")


class tbl_artist(models.Model):
    artist_name=models.CharField(max_length=50)
    artist_gender=models.CharField(max_length=50)
    artist_contact=models.CharField(max_length=50)
    artist_email=models.CharField(max_length=50)
    artist_address=models.CharField(max_length=500)
    artist_about=models.CharField(max_length=500)
    artist_password=models.CharField(max_length=50)
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    artist_photo = models.FileField(upload_to='Assets/ArtistPhoto/')
    artist_proof = models.FileField(upload_to='Assets/ArtistProof/')
    artist_status = models.IntegerField(default="0")
    artist_doj=models.DateField(auto_now_add=True)
    
    