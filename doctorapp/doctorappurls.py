from django.urls import path
from . import views

urlpatterns=[
    path("doctorapp/",views.doctorhome,name="doctorhome"),
    path("dviewprofile/",views.dviewprofile,name="dviewprofile"),
    path("myblog/",views.myblog,name="myblog"),
    path("viewblog/",views.viewblog,name="viewblog"),
    path("viewdrafts/",views.viewdrafts,name="viewdrafts"),
    ]