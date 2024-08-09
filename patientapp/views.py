from django.shortcuts import render,redirect
from mainapp.models import Patient
from django.views.decorators.cache import cache_control
from doctorapp.models import Blog
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def patienthome(request):
    try:
        if request.session["username"]!=None:
            username=request.session["username"]
            patientreg=Patient.objects.get(emailaddress=username)
            return render(request,"patienthome.html",locals())
    except KeyError:
        return redirect("mainapp:login")
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def pviewprofile(request):
    try:
        if request.session["username"]!=None:
            username=request.session["username"]
            pat=Patient.objects.get(emailaddress=username)
            if request.method=="POST":
                pprofilepic=request.FILES["pprofilepic"]
                firstname=request.POST["firstname"]
                lastname=request.POST["lastname"]
                emailaddress=request.POST["emailaddress"]
                password=request.POST["password"]
                state=request.POST['state']
                city=request.POST['city']
                pincode=request.POST['pincode']
                Patient.objects.all()
                return redirect("patientapp:patienthome")
            return render(request,"pviewprofile.html",locals())
    except KeyError:
        return redirect("mainapp:login")
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def viewblogs(request):
    try:
        if request.session["username"]!=None:
            username=request.session["username"]
            blog=Blog.objects.all()
            return render(request,"viewblogs.html",locals())
    except KeyError:
        return redirect("mainapp:login")