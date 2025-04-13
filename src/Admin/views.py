#from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect
from Admin.models import *
from User.models import *
from datetime import date

def district(request):
    dis=tbl_district.objects.all()
    if request.method=="POST":
        dis=request.POST.get("dist")
        tbl_district.objects.create(district_name=dis)
        return redirect('Admin:district')
    else:

     return render(request, 'Admin/district.html',{'district':dis})
    
def deletedistrict(request,did):
   tbl_district.objects.get(id=did).delete()
   return redirect('Admin:district')

def editdistrict(request,eid):
   editdata=tbl_district.objects.get(id=eid)
   if request.method=="POST":
      editdata.district_name=request.POST.get("dist")
      editdata.save()
      return redirect('Admin:district')
   else:
    return render(request,"Admin/district.html",{'edit':editdata})

def category(request):
    categ=tbl_category.objects.all()
    if request.method=="POST":
        categ=request.POST.get("cat")
        tbl_category.objects.create(category_name=categ)
        return redirect('Admin:category')
    else:

     return render(request, 'Admin/category.html',{'category':categ})
def deletecategory(request,did):
   tbl_category.objects.get(id=did).delete()
   return redirect('Admin:category')

def editcategory(request,eid):
   editdata=tbl_category.objects.get(id=eid)
   if request.method=="POST":
      editdata.category_name=request.POST.get("cat")
      editdata.save()
      return redirect('Admin:category')
   else:
    return render(request,"Admin/category.html",{'edit':editdata})


def adminregistration(request):
    ad=tbl_adminregistration.objects.all()
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        tbl_adminregistration.objects.create(name=name,email=email,password=password)
        return redirect('Admin:adminregisitration')

    return render(request, 'Admin/adminregistration.html',{'adminregistration':ad})

def deleteadminregistration(request,did):
   tbl_adminregistration.objects.get(id=did).delete()
   return redirect('Admin:adminregistration')

def editadminregistration(request,eid):
   editdata=tbl_adminregistration.objects.get(id=eid)
   if request.method=="POST":
      editdata.name=request.POST.get("name")
      editdata.email=request.POST.get("email")
      editdata.password=request.POST.get("password")
      editdata.save()
      return redirect('Admin:adminregistration')
   else:
    return render(request,"Admin/adminregistration.html",{'edit':editdata})
   
def Place(request):
   dis=tbl_district.objects.all()
   Pla=tbl_place.objects.all()
   if request.method=="POST":
      Place=request.POST.get("txt_place")
      district=tbl_district.objects.get(id=request.POST.get("sel_district"))
      tbl_place.objects.create(place_name=Place,district=district)
      return redirect('Admin:Place')
   else:
      return render(request, 'Admin/Place.html',{'district':dis,'place':Pla})
   
def subcategory(request):
   categ=tbl_category.objects.all()
   subcateg=tbl_subcategory.objects.all()
   if request.method=="POST":
      subcategory=request.POST.get("txt_subcategory")
      category=tbl_category.objects.get(id=request.POST.get("sel_category"))
      tbl_subcategory.objects.create(subcategory_name=subcategory,category=category)
      return redirect('Admin:subcategory')
   else:
      return render(request, 'Admin/subcategory.html',{'category':categ,'subcategory':subcateg})


def deletesubcategory(request,did):
   tbl_subcategory.objects.get(id=did).delete()
   return redirect('Admin:subcategory')

def editsubcategory(request,eid):
   editdata=tbl_subcategory.objects.get(id=eid)
   if request.method=="POST":
      editdata.subcategory_name=request.POST.get("txt_subcategory")
      editdata.save()
      return redirect('Admin:subcategory')
   else:
    return render(request,"Admin/subcategory.html",{'edit':editdata})


def deleteplace(request,did):
   tbl_place.objects.get(id=did).delete()
   return redirect('Admin:Place')

def editplace(request,eid):
   dis=tbl_district.objects.all()
   editdata=tbl_place.objects.get(id=eid)
   if request.method=="POST":
      editdata.place_name=request.POST.get("txt_place")
      editdata.district=tbl_district.objects.get(id=request.POST.get("sel_district"))
      editdata.save()
      return redirect('Admin:Place')
   else:
    return render(request,"Admin/Place.html",{'edit':editdata,'district':dis})
   

def viewcomplaint(request):
   complaint=tbl_complaint.objects.filter(technician__isnull=True,deliveryboy__isnull=True,shop__isnull=True)
   return render(request,'Admin/viewcomplaint.html',{'viewcomplaint':complaint})

def replynow(request, id):
   complaint=tbl_complaint.objects.get(id=id)
   if request.method=="POST":
      complaint.complaint_reply=request.POST.get("txt_reply")
      complaint.complaint_status=1
      complaint.reply_date=date.today()
      complaint.save()
      return redirect('Admin:viewcomplaint')
   else:
      return render(request,'Admin/replyshop.html')
   
def shopcomplaint(request):
   complaint=tbl_complaint.objects.filter(technician__isnull=True,deliveryboy__isnull=True,user__isnull=True)
   return render(request,'Admin/shopcomplaint.html',{'shopcomplaint':complaint})

def replyshop(request, id):
   complaint=tbl_complaint.objects.get(id=id)
   if request.method=="POST":
      complaint.complaint_reply=request.POST.get("txt_reply")
      complaint.complaint_status=1
      complaint.reply_date=date.today()
      complaint.save()
      return redirect('Admin:shopcomplaint')

   else:
      return render(request,'Admin/replyshop.html')
   


def techniciancomplaint(request):
   complaint=tbl_complaint.objects.filter(user__isnull=True,deliveryboy__isnull=True,shop__isnull=True)
   return render(request,'Admin/techniciancomplaint.html',{'techniciancomplaint':complaint})

def replytechnician(request, id):
   complaint=tbl_complaint.objects.get(id=id)
   if request.method=="POST":
      complaint.complaint_reply=request.POST.get("txt_reply")
      complaint.complaint_status=1
      complaint.reply_date=date.today()
      complaint.save()
      return redirect('Admin:techniciancomplaint')
   else:
      return render(request,'Admin/replytechnician.html')
   
def deliveryboycomplaint(request):
   complaint=tbl_complaint.objects.filter(technician__isnull=True,user__isnull=True,shop__isnull=True)
   return render(request,'Admin/deliveryboycomplaint.html',{'deliveryboycomplaint':complaint})

def replydeliveryboy(request, id):
   complaint=tbl_complaint.objects.get(id=id)
   if request.method=="POST":
      complaint.complaint_reply=request.POST.get("txt_reply")
      complaint.complaint_status=1
      complaint.reply_date=date.today()
      complaint.save()
      return redirect('Admin:deliveryboycomplaint')
   else:
      return render(request,'Admin/replydeliveryboy.html')
   

   
def viewshops(request):
   shop_reg=tbl_shop.objects.all()
   return render(request,'Admin/viewshops.html',{'viewshops':shop_reg})

def rejectshop(request, id):
      tbl_shop.objects.get(id=id).delete()
      return redirect('Admin:viewshops')

def approveshop(request, id):
      shop=tbl_shop.objects.get(id=id)
      shop.shop_status=1
      shop.save()
      return redirect('Admin:viewshops')

def viewdeliveryboy(request):
   deliveryboy_reg=tbl_deliveryboy.objects.all()
   return render(request,'Admin/viewdeliveryboy.html',{'viewdeliveryboy':deliveryboy_reg})

def rejectdeliveryboy(request, id):
      tbl_deliveryboy.objects.get(id=id).delete()
      return redirect('Admin:viewdeliveryboy')

def approvedeliveryboy(request, id):
      deliveryboy=tbl_deliveryboy.objects.get(id=id)
      deliveryboy.deliveryboy_status=1
      deliveryboy.save()
      return redirect('Admin:viewdeliveryboy')

def homepage(request):
    user=tbl_user.objects.all()
    return render(request,'Admin/homepage.html',{'users':user})

def viewtechnician(request):
   technician_reg=tbl_technician.objects.all()
   return render(request,'Admin/viewtechnician.html',{'viewtechnician':technician_reg})

def rejecttechnician(request, id):
      tbl_technician.objects.get(id=id).delete()
      return redirect('Admin:viewtechnician')

def approvetechnician(request, id):
      technician=tbl_technician.objects.get(id=id)
      technician.technician_status=1
      technician.save()
      return redirect('Admin:viewtechnician')



      
def logout(request):
    del request.session["aid"]
    return redirect("Guest:login")

   

   



