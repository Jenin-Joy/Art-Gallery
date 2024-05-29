from django.db import models
from Guest.models import *
from Artist.models import *
class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=500)
    complaint_details=models.CharField(max_length=500)
    complaint_postdate=models.DateField(auto_now_add=True)
    complaint_reply=models.CharField(max_length=500)
    complaint_replydate=models.DateField(null=True)
    complaint_status = models.IntegerField(default="0")
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE,null=True)    

class tbl_booking(models.Model):
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    work = models.ForeignKey(tbl_artistwork, on_delete=models.CASCADE)
    booking_status = models.IntegerField(default="0")
    booking_date = models.DateField(auto_now_add=True)

class tbl_programbooking(models.Model):
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    program = models.ForeignKey(tbl_artistprogram, on_delete=models.CASCADE)
    booking_status = models.IntegerField(default="0")
    booking_date = models.DateField(auto_now_add=True)
    booking_fordate = models.DateField(null=True)
    booking_description = models.CharField(max_length=50)

class tbl_rating(models.Model):
    rating_data=models.IntegerField()
    user_name=models.CharField(max_length=500)
    user_review=models.CharField(max_length=500)
    work=models.ForeignKey(tbl_artistwork,on_delete=models.CASCADE)
    datetime=models.DateTimeField(auto_now_add=True)

class tbl_new_booking(models.Model):
    booking_date = models.DateField(auto_now_add=True)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    booking_status=models.IntegerField(default=0)
    booking_totalamount=models.CharField(max_length=50,null=True)

class tbl_cart(models.Model):
    booking=models.ForeignKey(tbl_new_booking,on_delete=models.CASCADE)
    cart_status=models.CharField(max_length=5,default='0')
    cart_qty=models.CharField(max_length=100)
    product=models.ForeignKey(tbl_artistwork,on_delete=models.CASCADE)

class tbl_ticket_booking(models.Model):
    booking_date = models.DateField(auto_now_add=True)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    booking_status=models.IntegerField(default=0)
    booking_totalamount=models.CharField(max_length=50,null=True)

class tbl_tickets(models.Model):
    booking = models.ForeignKey(tbl_ticket_booking,on_delete=models.CASCADE)
    seat_no = models.IntegerField()