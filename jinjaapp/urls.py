from django.urls import path
from jinjaapp import views

urlpatterns=[
    path('',views.home,name='my_home'),
    path('about/',views.about,name='my_about'),
    path('contact/',views.contact,name='my_contact'),
    path('services/',views.services,name='my_services'),
    path('blog/',views.blog,name='my_blog'),


]