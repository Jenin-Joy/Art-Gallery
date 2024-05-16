from django.db import models

# Create your models here.
class tbl_district(models.Model):
    district_name=models.CharField(max_length=50)

class tbl_arttype(models.Model):
    arttype_name=models.CharField(max_length=50)

class tbl_place(models.Model):
    place_name=models.CharField(max_length=50)
    district = models.ForeignKey(tbl_district, on_delete=models.CASCADE)

class tbl_admin(models.Model):
    admin_name=models.CharField(max_length=50)
    admin_contact=models.CharField(max_length=50)
    admin_email=models.CharField(max_length=50)
    admin_password=models.CharField(max_length=50)

class tbl_category(models.Model):
    category_name=models.CharField(max_length=50)


class tbl_subcategory(models.Model):
    subcat_name=models.CharField(max_length=50)
    category = models.ForeignKey(tbl_category, on_delete=models.CASCADE)

class tbl_programtype(models.Model):
    programtype_name=models.CharField(max_length=50)

class tbl_event(models.Model):
    event_name=models.CharField(max_length=30)
    event_start_date=models.DateField()
    event_end_date=models.DateField()
    event_details=models.CharField(max_length=30)
    event_image=models.FileField(upload_to='Assets/EventPhoto/')
