from django.shortcuts import render,redirect
from . models import Login, Patient,Doctor
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def index(request):
     return render(request,"index.html")
def doctorreg(request):
    if request.method=="POST":
        firstname=request.POST["firstname"]
        lastname=request.POST["lastname"]
        emailaddress=request.POST["emailaddress"]
        password=request.POST["password"]
        state=request.POST['state']
        city=request.POST['city']
        pincode=request.POST['pincode']
        doctorreg=Doctor(firstname=firstname,lastname=lastname,emailaddress=emailaddress,password=password,state=state,city=city,pincode=pincode)
        doctorreg.save()
        log=Login(username=emailaddress,password=password,usertype="doctor")
        log.save()
        return render(request,"doctorreg.html",{"msg":"Registration is done"})
    return render(request,"doctorreg.html")
def patientreg(request):
    if request.method=="POST":
        pprofilepic=request.FILES["pprofilepic"]
        firstname=request.POST["firstname"]
        lastname=request.POST["lastname"]
        emailaddress=request.POST["emailaddress"]
        password=request.POST["password"]
        state=request.POST["state"]
        city=request.POST["city"]
        pincode=request.POST["pincode"]
        pat=Patient(pprofilepic=pprofilepic,firstname=firstname,lastname=lastname,emailaddress=emailaddress,password=password,state=state,city=city,pincode=pincode)
        pat.save()
        log=Login(username=emailaddress,password=password,usertype="patient")
        log.save()
        return render(request,"patientreg.html",{"msg":"Registration is done"})
    return render(request,"patientreg.html")
def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        try:
            obj=Login.objects.get(username=username,password=password)
            if obj is not None:
                if obj.usertype=='patient':
                   request.session["username"]=username
                   return redirect("patientapp:patienthome")
                elif obj.usertype=='doctor':
                    request.session["username"]=username
                    return redirect("doctorapp:doctorhome")
        except ObjectDoesNotExist:
            msg="Invalid User"
        return render(request,'login.html',{"msg":msg}) 
    return render(request,"login.html")
def blog(request):
     return render(request,"blog.html")