from django.urls import path
from . import views

urlpatterns=[
    path("doctorhome/",views.doctorhome,name="doctorhome"),
    path("dviewprofile/",views.dviewprofile,name="dviewprofile"),
    ]