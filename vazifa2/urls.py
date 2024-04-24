from django.urls import path
from .views import index,about,contact,service,price

urlpatterns = [

path('',index,name="index-page"),
path('about/',about,name= "about-page"),
path('contact/',contact,name= "contact-page"),
path('price/',price,name= "price-page"),
path('service/',service,name= "service-page")

]