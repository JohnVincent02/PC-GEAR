from django.urls import path
from User import views
app_name="User"
urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('myprofile/',views.Myprofile,name="myprofile"),
    path('Changepassword/',views.Changepassword,name="changepassword"),
    path('Editprofile/',views.Editprofile,name="editprofile"),
    path('Complaint/',views.Complaint,name="complaint"),
    path('viewcomplaint/',views.viewreply,name="viewcomplaint"),
    path('viewtechnician/',views.View_technician,name="viewtechnician"),
    path('request/<int:id>',views.Request,name="request"),
    path('deleterequest/<int:id>',views.deleterequest,name="deleterequest"),
    path('viewproducts',views.viewproducts,name="viewproducts"),
    path('myrequest/',views.myrequest,name="myrequest"),
    path("payment/<int:id>",views.payment,name="payment"),
    path('loader/',views.loader, name='loader'),
    path('paymentsuc/',views.paymentsuc, name='paymentsuc'), 
    path('ajaxsubcategory/',views.ajaxsubcategory,name="ajaxsubcategory"),
    path('ajaxproduct/',views.ajaxproduct,name="ajaxproduct"),
    path('Ajaxplace/',views.ajaxplace,name="ajaxplace"),


    path('addcart/<int:pid>',views.Addcart, name='addcart'),
    path('Mycart/',views.Mycart, name='Mycart'),
    path("DelCart/<int:did>", views.DelCart,name="delcart"),
    path("CartQty/", views.CartQty,name="cartqty"),
    path("productpayment/", views.productpayment,name="productpayment"),
    path("mybooking/",views.Mybooking,name="mybooking"),
    path("viewcartproducts/<int:id>",views.viewcartproducts,name="viewcartproducts"),
    path("feedback/<int:id>",views.feedback,name="feedback"),

    path('rating/<int:mid>',views.rating,name="rating"),  
    path('ajaxstar/',views.ajaxstar,name="ajaxstar"),
    path('starrating/',views.starrating,name="starrating"),
    path('bill/<int:bid>',views.bill,name="bill"),
    path('logout',views.logout,name="logout"),


]   