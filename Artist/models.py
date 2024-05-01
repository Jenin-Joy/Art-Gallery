from django.db import models
from Admin.models import *
from Guest.models import *
# Create your models here.

class tbl_artistwork(models.Model):
    artist = models.ForeignKey(tbl_artist,on_delete=models.CASCADE)
    arttype = models.ForeignKey(tbl_arttype,on_delete=models.CASCADE)
    work_caption = models.CharField(max_length=50)
    work_details = models.CharField(max_length=50)
    work_image = models.FileField(upload_to='Work_Photo/')
    work_price = models.CharField(max_length=50)
    work_status = models.IntegerField(default=0)
    work_date = models.DateField(auto_now_add=True)

class tbl_artistprogram(models.Model):
    artist = models.ForeignKey(tbl_artist,on_delete=models.CASCADE)
    programtype = models.ForeignKey(tbl_programtype,on_delete=models.CASCADE)
    program_caption = models.CharField(max_length=50)
    program_details = models.CharField(max_length=50)
    program_image = models.FileField(upload_to='Program_Photo/')
    program_price = models.CharField(max_length=50)
    program_status = models.IntegerField(default=0)
    program_date = models.DateField(auto_now_add=True)