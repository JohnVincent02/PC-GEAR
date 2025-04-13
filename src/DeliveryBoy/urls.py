from django.urls import path
from DeliveryBoy import views
app_name="DeliveryBoy"
urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('Editprofile/',views.Editprofile,name="editprofile"),
    path('deliveryboy_profile/',views.Myprofile,name="deliveryboy_profile"),
    path('Changepassword/',views.Changepassword,name="changepassword"),
    path('viewassignedwork/',views.ViewAssignedWork,name="viewassignedwork"),
    path('rejectdelivery/<int:id>',views.rejectdelivery,name="rejectdelivery"),
    path('acceptdelivery/<int:id>',views.acceptdelivery,name="acceptdelivery"),
    
    path('outofdelivery/<int:oid>',views.OutofDelivery,name="outofdelivery"),
    path('delivered/<int:did>',views.delivered,name="delivered"),
    path('Complaint/',views.Complaint,name="complaint"),
    path('viewcomplaint/',views.viewreply,name="viewcomplaint"),
    path('logout',views.logout,name="logout"),
   

 
 

]   