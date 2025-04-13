from django.urls import path
from Guest import views
app_name="Guest"
urlpatterns = [
    path('signupform/', views.signupform, name='signupform'),
    path('ajaxplace/', views.ajaxplace, name='ajaxplace'),
    path('login/', views.login, name='login'),
    path('shopsignupform/', views.shop_signupform, name='shop_signupform'),
    path('deliveryboysignupform/', views.deliveryboy_signupform, name='deliveryboy_signupform'),
    path('techniciansignupform/', views.technician_signupform, name='technician_signupform'),
    path('', views.index, name='index'),
    path('forgotpassword/',views.forgotpassword,name="forgotpassword"),
    path('otp/',views.otp,name="otp"),
    path('newpass/',views.newpass,name="newpass"),

]