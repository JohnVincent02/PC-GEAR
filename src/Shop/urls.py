from django.urls import path
from Shop import views
app_name="Shop"
urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('shop_profile/',views.Myprofile,name="myprofile"),
    path('Editprofile/',views.Editprofile,name="editprofile"),
    path('Changepassword/',views.Changepassword,name="changepassword"),
    path('ajaxsubcategory/',views.ajaxsubcategory,name="ajaxsubcategory"),
    
    path('addproducts/',views.Addproducts,name="addproducts"),
    path('deleteproducts/<int:id>',views.deleteproducts,name="deleteproducts"),
    path('addstock/<int:id>',views.addstock,name="addstock"),
    path('deletestock/<int:id>/<int:did>',views.deletestock,name="deletestock"),
    path('viewbooking/',views.Viewbooking,name="viewbooking"),
    path('viewdeliveryboy/<int:sid>',views.View_deliveryboy,name="viewdeliveryboy"),
    path('assigndelivery/<int:did>/<int:sid>',views.Assign_delivery,name="assigndelivery"),
    path('ajaxplace/', views.ajaxplace, name='ajaxplace'),
    path('viewfeedback/<int:id>',views.viewfeedback,name="viewfeedback"),
    path('reassign/<int:did>//<int:sid>',views.reassign,name="reassign"),
    path('Complaint/',views.Complaint,name="complaint"),
    path('viewcomplaint/',views.viewreply,name="viewcomplaint"),
    path('logout',views.logout,name="logout"),


   

]   