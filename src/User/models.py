from django.db import models


from Guest.models import *

from Shop.models import *

# Create your models here.
class tbl_complaint(models.Model):
    complaint_subject=models.CharField(max_length=30)
    complaint_desc=models.CharField(max_length=30)
    complaint_date=models.DateField(auto_now_add=True)
    complaint_reply=models.CharField(max_length=30)
    reply_date=models.DateField(null=True)
    complaint_status=models.IntegerField(default=0)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE,null=True)
    shop=models.ForeignKey(tbl_shop,on_delete=models.CASCADE,null=True)
    deliveryboy=models.ForeignKey(tbl_deliveryboy,on_delete=models.CASCADE,null=True)
    technician=models.ForeignKey(tbl_technician,on_delete=models.CASCADE,null=True)


class tbl_request(models.Model):
    to_date=models.DateField()
    req_desc=models.CharField(max_length=30)
    req_status=models.IntegerField(default=0)
    req_date=models.DateField(auto_now_add=True)
    workdone_date=models.DateField(null=True)
    req_amount=models.CharField(max_length=30)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    technician=models.ForeignKey(tbl_technician,on_delete=models.CASCADE)

class tbl_booking(models.Model):
    booking_date = models.DateField(auto_now_add=True)
    booking_amount = models.CharField(max_length=30)
    booking_status = models.IntegerField(default=0)
    delivered_date =models.DateField(null=True)
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    deliveryboy = models.ForeignKey(tbl_deliveryboy, on_delete=models.CASCADE,null=True)

class tbl_cart(models.Model):
    cart_qty = models.IntegerField(default=1)
    cart_status = models.IntegerField(default=0)
    product = models.ForeignKey(tbl_addproducts, on_delete=models.CASCADE)
    booking = models.ForeignKey(tbl_booking, on_delete=models.CASCADE)
    
class tbl_assign(models.Model):
    assign_date=models.DateField(auto_now_add=True)
    deliveryboy=models.ForeignKey(tbl_deliveryboy,on_delete=models.CASCADE)
    assign_status=models.IntegerField(default=0)
    booking=models.ForeignKey(tbl_booking,on_delete=models.CASCADE)

class tbl_feedback(models.Model):
    feedback_content = models.CharField(max_length=50)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    product=models.ForeignKey(tbl_addproducts,on_delete=models.CASCADE)

class tbl_rating(models.Model):
    rating_data=models.IntegerField(default=0)
    rating_datetime=models.DateField(auto_now_add=True)
    rating_review=models.CharField(max_length=100)
    product=models.ForeignKey(tbl_addproducts,on_delete=models.CASCADE)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
   