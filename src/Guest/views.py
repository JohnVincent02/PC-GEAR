from django.shortcuts import redirect, render
from Guest.models import *
from Admin.models import * 
import random
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
# Create your views here.
def signupform(request):
    dis=tbl_district.objects.all()
    Pla=tbl_place.objects.all()
    if request.method=="POST":
        name=request.POST.get("txt_name")
        address=request.POST.get("txt_address")
        contact=request.POST.get("txt_contact")
        email=request.POST.get("txt_email")
        photo=request.FILES.get("photo")
        gender=request.POST.get("gender")
        dob=request.POST.get("dob")
        password=request.POST.get("password")
        place=tbl_place.objects.get(id=request.POST.get("sel_place"))

        tbl_user.objects.create(user_name=name,
                                place=place,
                              
                                user_email=email,
                                user_contact=contact,
                                user_address=address,
                                user_photo=photo,
                                user_gender=gender,
                                user_dob=dob,
                                user_password=password)
        return redirect('Guest:signupform')
    else:
        return render(request, 'Guest/signupform.html',{'district':dis,'place':Pla})

def ajaxplace(request):
    disdata=tbl_district.objects.get(id=request.GET.get('did'))
    place=tbl_place.objects.filter(district=disdata)
    return render(request, 'Guest/AjaxPlace.html',{'plc':place})




def shop_signupform(request):
    dis=tbl_district.objects.all()
    Pla=tbl_place.objects.all()
    if request.method=="POST":
        name=request.POST.get("txt_shopname")
        address=request.POST.get("txt_shopaddress")
        contact=request.POST.get("txt_shopcontact")
        email=request.POST.get("txt_shopemail")
        proof=request.FILES.get("proof")
        license=request.FILES.get("license")
        password=request.POST.get("password")
        place=tbl_place.objects.get(id=request.POST.get("sel_place"))

        tbl_shop.objects.create(shop_name=name,
                                place=place,
                                shop_email=email,
                                shop_contact=contact,
                                shop_address=address,
                                shop_proof=proof,
                                shop_license=license,
                                shop_password=password)
        return redirect('Guest:shop_signupform')
    else:
        return render(request, 'Guest/shopsignupform.html',{'district':dis,'place':Pla})
    


def deliveryboy_signupform(request):
    dis=tbl_district.objects.all()
    Pla=tbl_place.objects.all()
    if request.method=="POST":
        name=request.POST.get("txt_deliveryboyname")
        address=request.POST.get("txt_deliveryboyaddress")
        contact=request.POST.get("txt_deliveryboycontact")
        email=request.POST.get("txt_deliveryboyemail")
        proof=request.FILES.get("proof")
        photo=request.FILES.get("photo")
        password=request.POST.get("password")
        place=tbl_place.objects.get(id=request.POST.get("sel_place"))

        tbl_deliveryboy.objects.create(deliveryboy_name=name,
                                place=place,
                                deliveryboy_email=email,
                                deliveryboy_contact=contact,
                                deliveryboy_address=address,
                                deliveryboy_proof=proof,
                                deliveryboy_photo=photo,
                                deliveryboy_password=password)
        return redirect('Guest:deliveryboy_signupform')
    else:
        return render(request, 'Guest/deliveryboysignupform.html',{'district':dis,'place':Pla})



def technician_signupform(request):
    dis=tbl_district.objects.all()
    Pla=tbl_place.objects.all()
    if request.method=="POST":
        name=request.POST.get("txt_technicianname")
        contact=request.POST.get("txt_techniciancontact")
        email=request.POST.get("txt_technicianemail")
        proof=request.FILES.get("proof")
        photo=request.FILES.get("photo")
        password=request.POST.get("password")
        place=tbl_place.objects.get(id=request.POST.get("sel_place"))
        
        tbl_technician.objects.create(technician_name=name,
                                place=place,
                               
                                technician_email=email,
                                technician_contact=contact,
                                technician_proof=proof,
                                technician_photo=photo,
                                technician_password=password)
        return redirect('Guest:technician_signupform')
    else:
        return render(request, 'Guest/techniciansignupform.html',{'district':dis,'place':Pla})





def login(request):

        if request.method=="POST":
            email=request.POST.get("txt_email")
            password=request.POST.get("txt_password")
            

            usercount=tbl_user.objects.filter(user_email=email,user_password=password). count()
            shopcount=tbl_shop.objects.filter(shop_email=email,shop_password=password). count()
            deliveryboycount=tbl_deliveryboy.objects.filter(deliveryboy_email=email,deliveryboy_password=password). count()
            admincount=tbl_adminregistration.objects.filter(email=email,password=password). count()
            technician=tbl_technician.objects.filter(technician_email=email,technician_password=password). count()

            if usercount > 0:
                user=tbl_user.objects.get(user_email=email,user_password=password)
                request.session["uid"]=user.id
                user.save()
                return redirect('User:homepage')
            
            elif admincount > 0:
                admin=tbl_adminregistration.objects.get(email=email,password=password)
                
                request.session["aid"]=admin.id
                admin.save()
                return redirect('Admin:homepage')
            

            elif shopcount > 0:
                shop=tbl_shop.objects.get(shop_email=email,shop_password=password)
                if shop.shop_status==1:

                    request.session["sid"]=shop.id
                    shop.save()
                    return redirect('Shop:homepage')
                
            elif deliveryboycount > 0:
                deliveryboy=tbl_deliveryboy.objects.get(deliveryboy_email=email,deliveryboy_password=password)
                if deliveryboy.deliveryboy_status==1:
                    request.session["did"]=deliveryboy.id
                    deliveryboy.save()
                    return redirect('DeliveryBoy:homepage')
                

            elif technician > 0:
                technician=tbl_technician.objects.get(technician_email=email,technician_password=password)
                if technician.technician_status==1:
                    request.session["tid"]=technician.id
                    technician.save()
                    return redirect('Technician:homepage')
                


                

                else:
                    return render(request,'Guest/login.html',{'msg':"Invalid Login"})
            else:
                return render(request,'Guest/login.html',{'msg':"Invalid Login"})
        else:
             return render(request,"Guest/login.html")

def index(request):
    return render(request,'Guest/index.html')

def forgotpassword(request):
    if request.method == "POST":
        email = request.POST.get("txt_email")
        user = tbl_user.objects.get(user_email=email)
        otp = random.randint(111111,999999)
        request.session["otp"] = otp
        request.session["fid"] = user.id
        send_mail(
            'Forgot password OTP', #subject
            "\rHello \r" + str(otp) +"\n This is the OTP to reset ur password.\n If you didn't ask to reset your password, you can ignore this email. \r\n Thanks. \r\n Your D MARKET team.",#body
            settings.EMAIL_HOST_USER,
            [email],
        )
        return render(request,"Guest/ForgotPassword.html",{"msg":email})
    else:
        return render(request,"Guest/ForgotPassword.html")
        

def otp(request):
    if request.method == "POST":
        inp_otp = int(request.POST.get("txt_otp"))
        if inp_otp == request.session["otp"]:
            return redirect("Guest:newpass")
        else:
            return render(request,"Guest/OTP.html",{"msg":"OTP Does not Matches..!!"})
    else:
        return render(request,"Guest/OTP.html")

def newpass(request):
    if request.method == "POST":
        user = tbl_user.objects.get(id=request.session["fid"])
        if request.POST.get("txt_new_pass") == request.POST.get("txt_con_pass"):
            user.user_password = request.POST.get("txt_con_pass")
            user.save()
            return render(request,"Guest/NewPassword.html",{"msg1":"Password Updated Sucessfully...."})
        else:
            return render(request,"Guest/NewPassword.html",{"msg":"Error in confirm password..!!!"})
    else:
        return render(request,"Guest/NewPassword.html")




