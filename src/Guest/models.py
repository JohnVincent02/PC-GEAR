from django.db import models
from Admin.models import *
from Guest.models import *

# Create your models here.
class tbl_user(models.Model):
    user_name=models.CharField(max_length=30)
    user_address=models.CharField(max_length=30)
    user_contact=models.CharField(max_length=30)
    user_email=models.CharField(max_length=30)
    user_photo=models.FileField(upload_to="Assets/File/User/")
    user_gender=models.CharField(max_length=30)
    user_dob=models.CharField(max_length=30)
    user_password=models.CharField(max_length=30)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)


class tbl_shop(models.Model):
    shop_name=models.CharField(max_length=30)
    shop_address=models.CharField(max_length=30)
    shop_contact=models.CharField(max_length=30)
    shop_email=models.CharField(max_length=30)
    shop_proof=models.FileField(upload_to="Assets/File/Shop/proof")
    shop_license=models.FileField(upload_to="Assets/File/Shop/license")
    shop_password=models.CharField(max_length=30)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    shop_status=models.IntegerField(default=0)

class tbl_login(models.Model):
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=30)

class tbl_deliveryboy(models.Model):
    deliveryboy_name=models.CharField(max_length=30)
    deliveryboy_address=models.CharField(max_length=30)
    deliveryboy_contact=models.CharField(max_length=30)
    deliveryboy_email=models.CharField(max_length=30)
    deliveryboy_proof=models.FileField(upload_to="Assets/File/Delivery_boy/proof")
    deliveryboy_photo=models.FileField(upload_to="Assets/File/Delivery_boy/license")
    deliveryboy_password=models.CharField(max_length=30)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    deliveryboy_status=models.IntegerField(default=0)

class tbl_technician(models.Model):
    technician_name=models.CharField(max_length=30)
    technician_contact=models.CharField(max_length=30)
    technician_email=models.CharField(max_length=30)
    technician_proof=models.FileField(upload_to="Assets/File/Technician/proof")
    technician_photo=models.FileField(upload_to="Assets/File/Technician/photo")
    technician_password=models.CharField(max_length=30)
    technician_status=models.IntegerField(default=0)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    
