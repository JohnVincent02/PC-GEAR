from django.shortcuts import render,redirect
from Guest.models import *
from Shop.models import *
from User.models import *
from django.db.models import Sum
# Create your views here.
def homepage(request):
    shop=tbl_shop.objects.get(id=request.session["sid"])

    return render(request,'Shop/homepage.html',{'shop':shop})
def Myprofile(request):
    shop=tbl_shop.objects.get(id=request.session["sid"])
    return render(request,'Shop/shop_profile.html',{'shop':shop})
def Editprofile(request):
    shop=tbl_shop.objects.get(id=request.session["sid"])
    if request.method=="POST":
        shop.shop_name=request.POST["txt_name"]
        shop.shop_email=request.POST["txt_email"]
        shop.shop_contact=request.POST["txt_contact"]
        shop.shop_address=request.POST["txt_address"]
        shop.save()
        return redirect('Shop:myprofile')
    else:

        return render(request,'Shop/EditProfile.html',{'shop': shop})
    
def Changepassword(request):
    shop=tbl_shop.objects.get(id=request.session["sid"])
    if request.method=="POST":

        if shop.shop_password==request.POST.get("txtpass"):
            if request.POST.get("txtpassnew")==request.POST.get("txtrepass"):
                shop.shop_password=request.POST.get("txtpassnew")
                shop.save()
                return redirect('Shop:changepassword')
            else:
                return render(request,'Shop/ChangePassword.html',{"msg":"Invalid"})
        else:
             return render(request,'Shop/ChangePassword.html',{"msg":"Invalid"})
    else:

        return render(request,'Shop/Changepassword.html',{'shop':shop})
    

def Addproducts(request):
    catdata=tbl_category.objects.all()
    products=tbl_addproducts.objects.filter(shop=request.session["sid"])
    shop=tbl_shop.objects.get(id=request.session["sid"])
    if request.method=="POST":
        name=request.POST.get("txt_productname")
        details=request.POST.get("txt_productdetails")
        photo=request.FILES.get("photo")
        price=request.POST.get("txt_productprice")
        category=request.POST.get("sel_category")
        sub_category=tbl_subcategory.objects.get(id=request.POST.get("sel_subcategory"))

        


        tbl_addproducts.objects.create(product_name=name,
                                       product_details=details,
                                       product_photo=photo,
                                       product_price=price,
                                       sub_category=sub_category,
                                       shop=shop)
        return redirect('Shop:addproducts')
    else:
        return render(request, 'Shop/addproducts.html',{'addproducts':products,'catdata':catdata,'shop':shop})
    
def ajaxsubcategory(request):
    category=tbl_category.objects.get(id=request.GET.get('did'))
    subcategory=tbl_subcategory.objects.filter(category=category)
    return render(request,'Shop/Ajaxsubcategory.html',{'cat':subcategory})

def deleteproducts(request, id):
      tbl_addproducts.objects.get(id=id).delete()
      return redirect('Shop:addproducts')

def addstock(request,id):
    stock=tbl_addstock.objects.filter(product=id)
    for i in stock:
        total_stock = tbl_addstock.objects.filter(product=i.product.id).aggregate(total=Sum('stock_quantity'))['total']
        total_cart = tbl_cart.objects.filter(product=i.product.id, cart_status__gte=1).aggregate(total=Sum('cart_qty'))['total']
        # print(total_stock)
        # print(total_cart)
        if total_stock is None:
            total_stock = 0
        if total_cart is None:
            total_cart = 0
        remining =  total_stock - total_cart
        i.total_stock=total_stock
        i.remining=remining
    if request.method=="POST":
        quantity=request.POST.get("txt_stock")
        productid=tbl_addproducts.objects.get(id=id)

        tbl_addstock.objects.create(product=productid,
                                    stock_quantity=quantity)
        return redirect('Shop:addstock', id)
    else:
        return render(request, 'Shop/addstock.html',{'addstock':stock,'id':id})
      
def deletestock(request, id, did):
      tbl_addstock.objects.get(id=id).delete()
    #   return redirect('Shop:addstock')
      return redirect('Shop:addstock', did)

def Viewbooking(request):
   viewbooking=tbl_cart.objects.filter(product__shop=request.session["sid"],booking__booking_status__gte=0,cart_status=1).order_by("-booking__booking_date")
   return render(request,'Shop/viewbooking.html',{'viewbooking':viewbooking})

def View_deliveryboy(request, sid):
    
    dis = tbl_district.objects.all()
    Pla = tbl_place.objects.all()
    
  
    booking = tbl_booking.objects.get(id=sid)
    
   
    if request.method == "POST":
       
        place = tbl_place.objects.get(id=request.POST.get("sel_place"))
        
       
        deliveryboy = tbl_deliveryboy.objects.filter(place=place).exclude(id__in=tbl_assign.objects.filter(booking=booking).values('deliveryboy_id'))
        
       
        return render(request, 'Shop/viewdeliveryboy.html', {'viewdeliveryboy': deliveryboy, 'sid': sid})
    
   
    else:
       
        deliveryboy = tbl_deliveryboy.objects.exclude(id__in=tbl_assign.objects.filter(booking=booking).values('deliveryboy_id'))
        return render(request, 'Shop/viewdeliveryboy.html', {'viewdeliveryboy': deliveryboy, 'dist': dis, 'sid': sid, 'booking': booking})


def ajaxplace(request):
    disdata=tbl_district.objects.get(id=request.GET.get('did'))
    place=tbl_place.objects.filter(district=disdata)
    
    return render(request, 'Guest/AjaxPlace.html',{'plc':place,})





def Assign_delivery(request, did, sid):
    booking = tbl_booking.objects.get(id=sid)
    if booking.booking_status == 2:
        deliveryboy = tbl_deliveryboy.objects.get(id=did)
        tbl_assign.objects.create(booking=booking, deliveryboy=deliveryboy)
        return render(request, 'Shop/viewdeliveryboy.html', {'msg': "Assigned", 'sid': sid})
    else:
        assign = tbl_assign.objects.filter(booking=booking).first() 
        if assign:
            assign.deliveryboy = tbl_deliveryboy.objects.get(id=did)
            booking.booking_status = 2  
            booking.save()  
            assign.save()  
        return render(request, 'Shop/viewdeliveryboy.html', {'msg': "Reassigned", 'sid': sid})


def viewfeedback(request, id):
   feedback=tbl_feedback.objects.filter(product=id)
   return render(request,'Shop/viewfeedback.html',{'viewfeedback':feedback})

def reassign(request,did,sid):
    booking=tbl_booking.objects.filter(id=sid,booking_status=4)
    assign=tbl_assign.objects.filter(booking=booking)
    assign.deliveryboy=tbl_deliveryboy.objects.get(id=did)
    booking.booking_status == 2
    # deliveryboy=tbl_deliveryboy.objects.get(id=did)
    # tbl_assign.objects.create(booking=booking,deliveryboy=deliveryboy)
    # booking.booking_status == 4
    return render(request,'Shop/viewdeliveryboy.html',{'msg':"Reassigned",'sid':sid})

def Complaint(request):
    shop=tbl_shop.objects.get(id=request.session['sid'])
    subject=tbl_complaint.objects.filter(id=request.session['sid'])
    if request.method=="POST":
        subject=request.POST["txt_subject"]
        complaint=request.POST["txt_complaint"]
        
        tbl_complaint.objects.create(complaint_subject=subject,complaint_desc=complaint,shop=shop)

        return redirect('Shop:complaint')
    else:

        return render(request,'Shop/complaint.html')
    
def viewreply(request):

    subject=tbl_complaint.objects.filter(shop=request.session['sid'])
        
    return render(request,'Shop/viewcomplaint.html',{'subject':subject})
    


def logout(request):
    del request.session["sid"]
    return redirect("Guest:login")



    





