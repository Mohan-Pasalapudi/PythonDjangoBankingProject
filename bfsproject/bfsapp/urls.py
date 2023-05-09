from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('adminlogin', views.adminlogin, name='adminlogin'),
    path('checkadminlogin', views.checkadminlogin, name="checkadminlogin"),
    path('adminhome', views.adminhome, name="adminhome"),
    path('empregistration', views.empregistration, name="empregistration"),
    path('checkemplogin', views.checkemplogin, name="checkemplogin"),
    path('emplogin', views.emplogin, name="emplogin"),
    path('cuslogin', views.cuslogin, name="cuslogin"),
    path('cusregistration', views.cusregistration, name="cusregistration"),
    path('checkcuslogin', views.checkcuslogin, name="checkcuslogin"),
    path('emphome', views.emphome, name="emphome"),
    path('cushome', views.cushome, name="cushome"),
    path('about', views.about, name="about"),
    path('emplogout', views.emplogout, name='emplogout'),
    path('cuslogout', views.cuslogout, name="cuslogout"),
    path('viewcus', views.viewcustomers, name="viewcus"),
    path('newcustomer', views.newcustomer, name="newcustomer"),
    path('adminhome', views.adminhome, name="adminhome"),
    path('viewemps', views.viewemployees, name="viewemps"),
    path('adminlogout', views.adminlogout, name='adminlogout'),
    path('empaddmoney', views.empaddmoney, name='empaddmoney'),
    path('transfer', views.transfer, name='transfer'),
    path('transactions', views.transactions, name='transactions'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
