from django.shortcuts import render,redirect
from Guest.models import *
from DeliveryBoy.models import *
from User.models import *
from datetime import date
# Create your views here.
def homepage(request):
    return render(request,'DeliveryBoy/homepage.html')


def Myprofile(request):
    deliveryboy=tbl_deliveryboy.objects.get(id=request.session["did"])
    return render(request,'DeliveryBoy/deliveryboy_profile.html',{'deliveryboy':deliveryboy})


def Editprofile(request):
    deliveryboy=tbl_deliveryboy.objects.get(id=request.session["did"])
    if request.method=="POST":
        deliveryboy.deliveryboy_name=request.POST["txt_name"]
        deliveryboy.deliveryboy_email=request.POST["txt_email"]
        deliveryboy.deliveryboy_contact=request.POST["txt_contact"]
        deliveryboy.deliveryboy_address=request.POST["txt_address"]
        deliveryboy.save()
        return redirect('DeliveryBoy:myprofile')
    else:

        return render(request,'DeliveryBoy/EditProfile.html',{'deliveryboy': deliveryboy})
    

def Changepassword(request):
    deliveryboy=tbl_deliveryboy.objects.get(id=request.session["did"])
    if request.method=="POST":

        if deliveryboy.deliveryboy_password==request.POST.get("txtpass"):
            if request.POST.get("txtpassnew")==request.POST.get("txtrepass"):
                deliveryboy.deliveryboy_password=request.POST.get("txtpassnew")
                deliveryboy.save()
                return redirect('DeliveryBoy:changepassword')
            else:
                return render(request,'DeliveryBoy/ChangePassword.html',{"msg":"Invalid"})
        else:
             return render(request,'DeliveryBoy/ChangePassword.html',{"msg":"Invalid"})
    else:

        return render(request,'DeliveryBoy/Changepassword.html',{'deliveryboy':deliveryboy})
    
def ViewAssignedWork(request):
   assign=tbl_assign.objects.filter(deliveryboy=request.session["did"])
   return render(request,'Deliveryboy/viewassignedwork.html',{'assign':assign})

def acceptdelivery(request, id):
   accept_assigns=tbl_booking.objects.get(id=id)
   accept_assigns.booking_status=3
   accept_assigns.save()
   return render(request,'DeliveryBoy/viewassignedwork.html',{'msg':"accept_assigns"})

def rejectdelivery(request, id):
    reject_assigns=tbl_booking.objects.get(id=id)
    reject_assigns.booking_status=4
    reject_assigns.save()
    return render(request,'DeliveryBoy/viewassignedwork.html',{'msg':"reject_assigns"})

def OutofDelivery(request, oid):
   print(oid)
   outofdelivery=tbl_booking.objects.get(id=oid)
   print(outofdelivery)
   outofdelivery.booking_status=5
   print(outofdelivery.booking_status)
   outofdelivery.save()
   return render(request,'DeliveryBoy/viewassignedwork.html',{'msg':"outofdelivery"})

def delivered(request, did):
   delivered=tbl_booking.objects.get(id=did)
   delivered.booking_status=6
   delivered.delivered_date=date.today()
   delivered.save()
   return render(request,'DeliveryBoy/viewassignedwork.html',{'msg':"delivered"})

def Complaint(request):
    deliveryboy=tbl_deliveryboy.objects.get(id=request.session['did'])
    subject=tbl_complaint.objects.filter(id=request.session['did'])
    if request.method=="POST":
        subject=request.POST["txt_subject"]
        complaint=request.POST["txt_complaint"]
        
        tbl_complaint.objects.create(complaint_subject=subject,complaint_desc=complaint,deliveryboy=deliveryboy)

        return redirect('DeliveryBoy:complaint')
    else:

        return render(request,'DeliveryBoy/complaint.html')
    
def viewreply(request):

    subject=tbl_complaint.objects.filter(deliveryboy=request.session['did'])
        
    return render(request,'DeliveryBoy/viewcomplaint.html',{'subject':subject})

def logout(request):
    del request.session["did"]
    return redirect("Guest:login")

