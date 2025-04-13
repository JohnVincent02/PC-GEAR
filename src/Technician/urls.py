from django.urls import path
from Technician import views
app_name="Technician"
urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('technician_profile/',views.Myprofile,name="myprofile"),
    path('Editprofile/',views.Editprofile,name="editprofile"),
    path('Changepassword/',views.Changepassword,name="changepassword"),
    path('viewrequest/',views.ViewRequest,name="viewrequest"),
    path('rejectrequest/<int:id>',views.RejectRequest,name="rejectrequest"),
    path('acceptrequest/<int:id>',views.AcceptRequest,name="acceptrequest"),
    path('workcompleted/<int:id>',views.WorkCompleted,name="workcompleted"),
    path('payment/<int:rid>',views.Payment,name="payment"),
    path('Complaint/',views.Complaint,name="complaint"),
    path('viewcomplaint/',views.viewreply,name="viewcomplaint"),
    path('logout',views.logout,name="logout"),



]

