from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('patientreg/',views.patientreg,name="patientreg"),
    path('doctorreg/',views.doctorreg,name="doctorreg"),
    path('login/',views.login,name="login"),
]