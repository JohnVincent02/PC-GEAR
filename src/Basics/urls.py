#from django.urls import path,include

#urlpatterns = [
#]

from django.urls import path
from . import views

urlpatterns = [
    path('calculator/', views.calculator, name='calculator'),
]

