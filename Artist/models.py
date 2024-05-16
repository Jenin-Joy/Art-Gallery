from django.db import models
from Admin.models import *
from Guest.models import *
# Create your models here.

class tbl_artistwork(models.Model):
    artist = models.ForeignKey(tbl_artist,on_delete=models.CASCADE)
    arttype = models.ForeignKey(tbl_arttype,on_delete=models.CASCADE)
    work_caption = models.CharField(max_length=50)
    work_details = models.CharField(max_length=50)
    work_image = models.FileField(upload_to='Assets/Work_Photo/')
    work_price = models.CharField(max_length=50)
    work_status = models.IntegerField(default=0)
    work_date = models.DateField(auto_now_add=True)
    work_stock= models.IntegerField(default=0)

class tbl_artistprogram(models.Model):
    artist = models.ForeignKey(tbl_artist,on_delete=models.CASCADE)
    programtype = models.ForeignKey(tbl_programtype,on_delete=models.CASCADE)
    program_caption = models.CharField(max_length=50)
    program_details = models.CharField(max_length=50)
    program_image = models.FileField(upload_to='Assets/Program_Photo/')
    program_price = models.CharField(max_length=50)
    program_status = models.IntegerField(default=0)
    program_date = models.DateField(auto_now_add=True)

class tbl_artistprogram_video(models.Model):
    program_video = models.FileField(upload_to='Assets/Program_video/')
    program = models.ForeignKey(tbl_artistprogram, on_delete=models.CASCADE)

class tbl_feedback(models.Model):
    feedback = models.CharField(max_length=100)
    artist = models.ForeignKey(tbl_artist, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)