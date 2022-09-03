from django.contrib import admin
from django.urls import path
from home import views
# from views import mainpage

urlpatterns = [
    path('', views.index,name='home'),
    path('about', views.about,name='about'),
    path('contact', views.contact,name='contact'),
    path('uregister', views.uregister,name='uregister'),
    path('ulogin', views.ulogin,name='ulogin'),
    path('ulogout', views.ulogout,name='ulogout'),
    path('xyz/',views.bot_search,name='bot_search')
]
