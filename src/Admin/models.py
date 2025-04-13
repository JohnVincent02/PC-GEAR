from django.db import models

class tbl_district(models.Model):
    district_name=models.CharField(max_length=40)

class tbl_category(models.Model):
    category_name=models.CharField(max_length=30)
    
class tbl_adminregistration(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=30)

class tbl_place(models.Model):
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)
    place_name=models.CharField(max_length=40)

class tbl_subcategory(models.Model):
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)
    subcategory_name=models.CharField(max_length=40)





