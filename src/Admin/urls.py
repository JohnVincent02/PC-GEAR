#from django.urls import path,include

#urlpatterns = [
#]

from django.urls import path
from Admin import views
app_name="Admin"
urlpatterns = [
    path('district/', views.district, name='district'),
    path('deletedistrict/<int:did>',views.deletedistrict,name="deletedistrict"),
    path('editdistrict/<int:eid>',views.editdistrict,name="editdistrict"),
    path('category/', views.category, name='category'),
    path('deletecategory/<int:did>',views.deletecategory,name="deletecategory"),
    path('editcategory/<int:eid>',views.editcategory,name="editcategory"),

    path('adminregistration/', views.adminregistration, name='adminregistration'),
    path('deleteadminregistration/<int:did>',views.deleteadminregistration,name="deleteadminregistration"),
    path('editadminregistration/<int:eid>',views.editadminregistration,name="editadminregistration"),
    path('Place/',views.Place,name="Place"),
    path('subcategory/',views.subcategory,name="subcategory"),
    path('deletesubcategory/<int:did>',views.deletesubcategory,name="deletesubcategory"),
    path('editsubcategory/<int:eid>',views.editsubcategory,name="editsubcategory"),
    path('deleteplace/<int:did>',views.deleteplace,name="deleteplace"),
    path('editplace/<int:eid>',views.editplace,name="editplace"),

    path('viewcomplaint/',views.viewcomplaint,name="viewcomplaint"),
    path('replynow/<int:id>', views.replynow, name='replynow'),

    path('shopcomplaint/',views.shopcomplaint,name="shopcomplaint"),
    path('replyshop/<int:id>', views.replyshop, name='replyshop'),

    path('techniciancomplaint/',views.techniciancomplaint,name="techniciancomplaint"),
    path('replytechnician/<int:id>', views.replytechnician, name='replytechnician'),

    path('deliveryboycomplaint/',views.deliveryboycomplaint,name="deliveryboycomplaint"),
    path('replydeliveryboy/<int:id>', views.replydeliveryboy, name='replydeliveryboy'),

    

    path('viewshops/',views.viewshops,name="viewshops"),
    path('rejectshop/<int:id>',views.rejectshop,name="rejectshop"),
    path('approveshop/<int:id>',views.approveshop,name="approveshop"),

    path('viewdeliveryboy/',views.viewdeliveryboy,name="viewdeliveryboy"),
    path('rejectdeliveryboy/<int:id>',views.rejectdeliveryboy,name="rejectdeliveryboy"),
    path('approvedeliveryboy/<int:id>',views.approvedeliveryboy,name="approvedeliveryboy"),

    path('homepage/', views.homepage, name='homepage'),

    path('viewtechnician/',views.viewtechnician,name="viewtechnician"),
    path('rejecttechnician/<int:id>',views.rejecttechnician,name="rejecttechnician"),
    path('approvetechnician/<int:id>',views.approvetechnician,name="approvetechnician"),

    path('logout/',views.logout,name="logout")
    

    
]
