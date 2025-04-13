from django.db import models

from Admin.models import *
from Guest.models import *




# Create your models here.
class tbl_addproducts(models.Model):
    product_name=models.CharField(max_length=30)
    product_details=models.CharField(max_length=30)
    product_photo=models.FileField(upload_to="Assets/File/Shop/product photo")
    product_price=models.CharField(max_length=30)
    sub_category=models.ForeignKey(tbl_subcategory,on_delete=models.CASCADE)
    shop=models.ForeignKey(tbl_shop,on_delete=models.CASCADE)

class tbl_addstock(models.Model):
    stock_quantity=models.CharField(max_length=30)
    product=models.ForeignKey(tbl_addproducts,on_delete=models.CASCADE)


    