from django.shortcuts import render,redirect
from Guest.models import *
from Technician.models import *
from User.models import *

# Create your views here.


def homepage(request):
    technician=tbl_technician.objects.get(id=request.session['tid'])
    return render(request,'Technician/homepage.html',{'technician':technician})

def Myprofile(request):
    technician=tbl_technician.objects.get(id=request.session["tid"])
    return render(request,'Technician/technician_profile.html',{'technician':technician})

def Editprofile(request):
    technician=tbl_technician.objects.get(id=request.session["tid"])
    if request.method=="POST":
        technician.technician_name=request.POST["txt_name"]
        technician.technician_email=request.POST["txt_email"]
        technician.technician_contact=request.POST["txt_contact"]
        technician.save()
        return redirect('Technician:myprofile')
    else:

        return render(request,'Technician/EditProfile.html',{'technician': technician})
    
def Changepassword(request):
    technician=tbl_technician.objects.get(id=request.session["tid"])
    if request.method=="POST":

        if technician.technician_password==request.POST.get("txtpass"):
            if request.POST.get("txtpassnew")==request.POST.get("txtrepass"):
                technician.technician_password=request.POST.get("txtpassnew")
                technician.save()
                return redirect('Technician:changepassword')
            else:
                return render(request,'Technician/ChangePassword.html',{"msg":"Invalid"})
        else:
             return render(request,'Technician/ChangePassword.html',{"msg":"Invalid"})
    else:

        return render(request,'Technician/Changepassword.html',{'deliveryboy':technician})
    
def ViewRequest(request):
   req_view=tbl_request.objects.filter(technician=request.session["tid"])
   user_details=tbl_user.objects.all()
   return render(request,'Technician/viewrequest.html',{'viewrequest':req_view,'userdetails':user_details})

def AcceptRequest(request,id):
      acceptrequest=tbl_request.objects.get(id=id)
      acceptrequest.req_status=1
      acceptrequest.save()
      return redirect('Technician:viewrequest')


def RejectRequest(request, id):
      rejectrequest=tbl_request.objects.get(id=id)
      rejectrequest.req_status=2
      rejectrequest.save()
      return redirect('Technician:viewrequest')

def WorkCompleted(request, id):
      workcompleted=tbl_request.objects.get(id=id)
      workcompleted.req_status=3
      workcompleted.workdone_date=date.today()
      workcompleted.save()
      return redirect('Technician:viewrequest')


def Payment(request,rid):
    payment=tbl_request.objects.get(id=rid)
    if request.method=="POST":
        payment.req_amount=request.POST.get("txt_amount")
        payment.save()
        return redirect('Technician:viewrequest')
    else:
        return render(request, 'Technician/payment.html')
    

def Complaint(request):
    technician=tbl_technician.objects.get(id=request.session['tid'])
    subject=tbl_complaint.objects.filter(id=request.session['tid'])
    if request.method=="POST":
        subject=request.POST["txt_subject"]
        complaint=request.POST["txt_complaint"]
        
        tbl_complaint.objects.create(complaint_subject=subject,complaint_desc=complaint,technician=technician)

        return redirect('Technician:complaint')
    else:

        return render(request,'Technician/complaint.html')
    
def viewreply(request):

    subject=tbl_complaint.objects.filter(technician=request.session['tid'])
        
    return render(request,'Technician/viewcomplaint.html',{'subject':subject})

def logout(request):
    del request.session["tid"]
    return redirect("Guest:login")