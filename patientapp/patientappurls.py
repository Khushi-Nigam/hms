from django.urls import path
from . import views

urlpatterns=[
    path("patienthome/",views.patienthome,name="patienthome"),
    path("pviewprofile/",views.pviewprofile,name="pviewprofile"),
    path("viewblogs/",views.viewblogs,name="viewblogs"),
    ]