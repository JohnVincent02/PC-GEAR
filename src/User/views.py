from django.shortcuts import render,redirect
from Guest.models import *
from User.models import *
from Shop.models import *
from Admin.models import *
from django.db.models import Sum
from django.http import JsonResponse
from datetime import datetime
from django.db.models import Q
# Create your views here.
def homepage(request):
    if 'uid' in request.session:
        user=tbl_user.objects.get(id=request.session['uid'])
        return render(request,'User/homepage.html',{'user':user})
    else:
        return redirect('Guest:login')
    

def Myprofile(request):
    if 'uid' in request.session:
        user=tbl_user.objects.get(id=request.session["uid"])
        return render(request,'User/myprofile.html',{'user':user})
    else:
        return redirect('Guest:login')

def logout(request):
    del request.session["uid"]
    return redirect("Guest:login")


def Editprofile(request):
    if 'uid' in request.session:
        user=tbl_user.objects.get(id=request.session["uid"])
        if request.method=="POST":
            user.user_name=request.POST["txt_name"]
            user.user_email=request.POST["txt_email"]
            user.user_contact=request.POST["txt_contact"]
            user.user_address=request.POST["txt_address"]
            user.save()
            return redirect('User:myprofile')
        else:

            return render(request,'User/EditProfile.html',{'user': user})
    else:
        return redirect('Guest:login')

def Changepassword(request):
    if 'uid' in request.session:
        user=tbl_user.objects.get(id=request.session["uid"])
        if request.method=="POST":

            if user.user_password==request.POST.get("txtpass"):
                if request.POST.get("txtpassnew")==request.POST.get("txtrepass"):
                    user.user_password=request.POST.get("txtpassnew")
                    user.save()
                    return redirect('User:changepassword')
                else:
                    return render(request,'User/ChangePassword.html',{"msg":"Invalid"})
            else:
                return render(request,'User/ChangePassword.html',{"msg":"Invalid"})
        else:

         return render(request,'User/Changepassword.html',{'user':user})
    

def Complaint(request):
    if 'uid' in request.session:
        user=tbl_user.objects.get(id=request.session['uid'])
        subject=tbl_complaint.objects.filter(id=request.session['uid'])
        if request.method=="POST":
            subject=request.POST["txt_subject"]
            complaint=request.POST["txt_complaint"]
        
            tbl_complaint.objects.create(complaint_subject=subject,complaint_desc=complaint,user=user)

            return redirect('User:complaint')
        else:
            return render(request,'User/complaint.html')
    else:
        return redirect('Guest:login')

def viewreply(request):
    if 'uid' in request.session:

        subject=tbl_complaint.objects.filter(user=request.session['uid'])
        
        return render(request,'User/viewcomplaint.html',{'subject':subject})
    else:
        return redirect('Guest:login')

def View_technician(request):
    if 'uid' in request.session:
        dis = tbl_district.objects.all()
        pla = tbl_place.objects.all()
    
        if request.method == "POST":
            selected_place_id = request.POST.get("sel_place")
            selected_place = tbl_place.objects.get(id=selected_place_id)
            technicians = tbl_technician.objects.filter(place=selected_place)
            return render(request, 'User/viewtechnician.html', {
                'viewtechnician': technicians,
                'dist': dis,
                'plc': pla,
                'selected_place_id': int(selected_place_id),
                'selected_district_id': selected_place.district.id,
            })
    
    # GET request - show all technicians
        all_technicians = tbl_technician.objects.all()
        return render(request, 'User/viewtechnician.html', {
            'viewtechnician': all_technicians,
            'dist': dis,
            'plc': pla
        })
    else:
        return redirect('Guest:login')

def Request(request,id):
    if 'uid' in request.session:
        user=tbl_user.objects.get(id=request.session['uid'])
        technician=tbl_technician.objects.get(id=id)
        request_technician=tbl_request.objects.all()
        if request.method=="POST":
            to_date=request.POST.get("txt_todate")
            req_desc=request.POST.get("txt_req_desc")
            tbl_request.objects.create(to_date=to_date,
                                        req_desc=req_desc,
                                        user=user,technician=technician
                                        )
            return render(request, 'User/request.html',{'request':request_technician,'technician':technician,'id':id})

        else:
            return render(request, 'User/request.html',{'request':request_technician,'technician':technician})
    else:
        return redirect('Guest:login')
    
def deleterequest(request, id):
    if 'uid' in request.session:
        tbl_request.objects.get(id=id).delete()
        return redirect('User:myrequest')
    else:
        return redirect('Guest:login')
    
def viewproducts(request):
    # product=tbl_addproducts.objects.all()
    if 'uid' in request.session:

        category=tbl_category.objects.all()
        district=tbl_district.objects.all()
        ar=[1,2,3,4,5]
        parry=[]
        avg=0
        product= tbl_addproducts.objects.all()
   
        for i in product:
            tot=0
            ratecount=tbl_rating.objects.filter(product=i.id).count()
            if ratecount>0:
                ratedata=tbl_rating.objects.filter(product=i.id)
                for j in ratedata:
                    tot=tot+j.rating_data
                    avg=tot//ratecount
                #print(avg)
                parry.append(avg)
            else:
                parry.append(0)
        # print(parry)
            datas=zip(product,parry)
        return render(request,'User/viewproducts.html',{'viewproducts':datas,'ar':ar,'category':category,'district':district})
    else:
        return redirect('Guest:login')   
#    return render(request,'User/viewproducts.html',{'viewproducts':product})



def ajaxsubcategory(request):
    if 'uid' in request.session:    
        category=tbl_category.objects.get(id=request.GET.get('did'))
        subcategory=tbl_subcategory.objects.filter(category=category)
        return render(request,'Shop/Ajaxsubcategory.html',{'cat':subcategory})
    else:
        return redirect('Guest:login') 


def ajaxproduct(request):
    if 'uid' in request.session:  
        category = request.GET.get("cid")
        subcategory = request.GET.get('sid')
        name = request.GET.get("name")
        place = request.GET.get("pid")
        district = request.GET.get("did")
        filter_conditions = Q()
        if category:
            filter_conditions &= Q(sub_category__category=category)
        if subcategory:
            filter_conditions &= Q(sub_category=subcategory)
        if name:
            filter_conditions &= Q(product_name__istartswith=name)
        if district:
            filter_conditions &= Q(shop__place__district=district)
        if place:
                filter_conditions &= Q(shop__place=place)
        product = tbl_addproducts.objects.filter(filter_conditions)
        ar=[1,2,3,4,5]
        parry=[]
        avg=0
        for i in product:
            tot=0
            ratecount=tbl_rating.objects.filter(product=i.id).count()
            if ratecount>0:
                ratedata=tbl_rating.objects.filter(product=i.id)
                for j in ratedata:
                    tot=tot+j.rating_data
                    avg=tot//ratecount
                    #print(avg)
                parry.append(avg)
            else:
                parry.append(0)
            # print(parry)
        datas=zip(product,parry)
        return render(request,'User/Ajaxproduct.html',{'product':datas,'ar':ar})
    else:
        return redirect('Guest:login')


def ajaxplace(request): 
    if 'uid' in request.session:  
        district=tbl_district.objects.get(id=request.GET.get('did'))
        place=tbl_place.objects.filter(district=district)
        return render(request,'Shop/AjaxPlace.html',{'pla':place})
    else:
        return redirect('Guest:login')
    

def myrequest(request):
    if 'uid' in request.session:      
        technician=tbl_technician.objects.all()
        myrequest=tbl_request.objects.filter(user=request.session['uid'])
        return render(request,'User/myrequest.html',{'myrequest':myrequest,'technician':technician})
    else:
        return redirect('Guest:login')

def payment(request,id):
    if 'uid' in request.session:      

        requestamount= tbl_request.objects.get(id=id)
                #    scrap = tbl_Scrap.objects.get(id=booking.scarp.id)
        amount = requestamount.req_amount
        if request.method == "POST":
            requestamount.req_status = 4
            requestamount.save()
            return redirect("User:loader")
        else:
            return render(request,"User/Payment.html", {"total":amount})
    else:
        return redirect('Guest:login')
    

def loader(request):
    if 'uid' in request.session:  
        return render(request,"User/Loader.html")
    else:
        return redirect('Guest:login')

def paymentsuc(request):
    if 'uid' in request.session:    
        return render(request,"User/Payment_suc.html")
    else:
        return redirect('Guest:login')

# def AddCart(request):
#     cart=tbl_addproducts.objects.all()
#     return render(request,"User/addcart.html", {"addcart":cart})
    
def Addcart(request,pid):
    if 'uid' in request.session:    

        productdata=tbl_addproducts.objects.get(id=pid)
        userdata=tbl_user.objects.get(id=request.session["uid"])
        bookingcount=tbl_booking.objects.filter(user=userdata,booking_status=0).count()
        if bookingcount>0:
            bookingdata=tbl_booking.objects.get(user=userdata,booking_status=0)
            cartcount=tbl_cart.objects.filter(booking=bookingdata,product=productdata).count()
            if cartcount>0:
                msg="Already added"
                return render(request,"User/viewproducts.html",{'msg':msg})
            else:
                tbl_cart.objects.create(booking=bookingdata,product=productdata)
                msg="Added To cart"
                return render(request,"User/viewproducts.html",{'msg':msg})
        else:
            bookingdata = tbl_booking.objects.create(user=userdata)
            tbl_cart.objects.create(booking=tbl_booking.objects.get(id=bookingdata.id),product=productdata)
            msg="Added To cart"
            return render(request,"User/viewproducts.html",{'msg':msg})
    else:
        return redirect('Guest:login')
    

def Mycart(request):
    if 'uid' in request.session:    
        if "uid" in request.session:
            if request.method=="POST":
                bookingdata=tbl_booking.objects.get(id=request.session["bookingid"])
                bookingdata.booking_amount=request.POST.get("carttotalamt")
                bookingdata.booking_status=1
                bookingdata.save()
                cart = tbl_cart.objects.filter(booking=bookingdata)
                for i in cart:
                    i.cart_status = 1
                    i.save()
                return redirect("User:productpayment")
            else:
                bookcount = tbl_booking.objects.filter(user=request.session["uid"],booking_status=0).count()
                if bookcount > 0:
                    book = tbl_booking.objects.get(user=request.session["uid"],booking_status=0)
                    request.session["bookingid"] = book.id
                    cart = tbl_cart.objects.filter(booking=book)
                    for i in cart:
                        total_stock = tbl_addstock.objects.filter(product=i.product.id).aggregate(total=Sum('stock_quantity'))['total']
                        total_cart = tbl_cart.objects.filter(product=i.product.id, cart_status=1).aggregate(total=Sum('cart_qty'))['total']
                        # print(total_stock)
                        # print(total_cart) 
                        if total_stock is None:
                            total_stock = 0
                        if total_cart is None:
                            total_cart = 0
                        total =  total_stock - total_cart
                        i.total_stock = total
                    return render(request,"User/MyCart.html",{'cartdata':cart})
                else:
                    return render(request,"User/MyCart.html")
        else:
            return redirect("Guest:LoginForm")
    else:
        return redirect('Guest:login')
    
    
def DelCart(request,did):       
    if 'uid' in request.session:  
        tbl_cart.objects.get(id=did).delete()
        return redirect("User:Mycart")
    else:
        return redirect('Guest:login')
    

def CartQty(request):
    if 'uid' in request.session:  
        qty=request.GET.get('QTY')
        cartid=request.GET.get('ALT')
        cartdata=tbl_cart.objects.get(id=cartid)
        cartdata.cart_qty=qty
        cartdata.save()
        return redirect("User:Mycart") 
    else:
        return redirect('Guest:login')  

def productpayment(request):
    if "uid" in request.session:
        bookingdata = tbl_booking.objects.get(id=request.session["bookingid"])
        amt = bookingdata.booking_amount
        if request.method == "POST":
            bookingdata.booking_status = 2
            bookingdata.save()
            return redirect("User:loader")
        else:
            return render(request,"User/Payment.html",{"total":amt})
    else:
        return redirect("Guest:login")
    
def Mybooking(request):
    if "uid" in request.session:
        book_product=tbl_cart.objects.filter(booking__user=request.session["uid"])
        return render(request,'User/mybooking.html',{'mybooking':book_product})
    else:
        return redirect("Guest:login")

def viewcartproducts(request,id):
    if "uid" in request.session:    
        product=tbl_cart.objects.filter(booking=id)

        return render(request,'User/viewcartproduct.html',{'product':product})
    else:
        return redirect("Guest:login")

def feedback(request, id):
    if "uid" in request.session:    

        feedback_content=tbl_feedback.objects.all()
        if request.method=="POST":
            feedback_content=request.POST.get("txt_feedback")
            product=tbl_addproducts.objects.get(id=id)
            user=tbl_user.objects.get(id=request.session["uid"      ])
            tbl_feedback.objects.create(feedback_content=feedback_content,product=product,
                                            user=user
                                            )
     

            return redirect('User:viewcartproducts',id)
        else:
            return render(request,'User/feedback.html',{'feedback_content':feedback_content})
    else:
        return redirect("Guest:login")


def rating(request,mid):
    if "uid" in request.session:        

        parray=[1,2,3,4,5]
        mid=mid
        # wdata=tbl_booking.objects.get(id=mid)
        
        counts=0
        counts=stardata=tbl_rating.objects.filter(product=mid).count()
        if counts>0:   
            res=0
            stardata=tbl_rating.objects.filter(product=mid).order_by('-rating_datetime')
            for i in stardata:
                res=res+i.rating_data
            avg=res//counts
            # print(avg)
            return render(request,"User/Rating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts})
        else:
            return render(request,"User/Rating.html",{'mid':mid})
    else:
        return redirect("Guest:login")

def ajaxstar(request):
    if "uid" in request.session:        
    
            parray=[1,2,3,4,5]
            rating_data=request.GET.get('rating_data')
            user=tbl_user.objects.get(id=request.session['uid'])
            rating_review=request.GET.get('rating_review')
            pid=request.GET.get('pid')
            # wdata=tbl_booking.objects.get(id=pid)
            tbl_rating.objects.create(user=user,rating_review=rating_review,rating_data=rating_data,product=tbl_addproducts.objects.get(id=pid))
            stardata=tbl_rating.objects.filter(product=pid).order_by('-rating_datetime')
            return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})
    else:
        return redirect("Guest:login")
    
def starrating(request):
    if "uid" in request.session:    
        r_len = 0
        five = four = three = two = one = 0
        # cdata = tbl_booking.objects.get(id=request.GET.get("pdt"))
        rate = tbl_rating.objects.filter(product=request.GET.get("pdt"))
        ratecount = tbl_rating.objects.filter(product=request.GET.get("pdt")).count()
        for i in rate:
            if int(i.rating_data) == 5:
                five = five + 1
            elif int(i.rating_data) == 4:
                four = four + 1
            elif int(i.rating_data) == 3:
                three = three + 1
            elif int(i.rating_data) == 2:
                two = two + 1
            elif int(i.rating_data) == 1:
                one = one + 1
            else:
                five = four = three = two = one = 0
            # print(i.rating_data)
            # r_len = r_len + int(i.rating_data)
        # rlen = r_len // 5
        # print(rlen)
        result = {"five":five,"four":four,"three":three,"two":two,"one":one,"total_review":ratecount}
        return JsonResponse(result)
    else:
        return redirect("Guest:login")
    


def bill(request, bid):
    if "uid" in request.session:    
        booking = tbl_booking.objects.get(id=bid)
        cart_items = tbl_cart.objects.filter(booking=booking)

        context = {
            'booking': booking,
            'cart_items': cart_items,
        }
        return render(request, 'User/Bill.html', context)
    else:
        return redirect("Guest:login")
   
