from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from main.models import Driver, User
from django.conf import settings

from utils import role_required, show_manytomany


def loginuser(req):
    if req.method == "POST":
        print(req.POST )
        uname = req.POST['uname']
        passw = req.POST['pass']
        user = authenticate(username=uname,password=passw)
        if user == None:
            return render(req,"auth/login.html",{"wrong" : True})
        login(req,user)
        return redirect(settings.LOGIN_REDIRECT_URL)
    return render(req,"auth/login.html")


@login_required(login_url='/login')
@role_required(User.ADMIN,User.DRIVER,User.PARENT)
def dashboard(request):
    role = request.user.role

    return render(request,'main/dashboard.html',{'role':role})


@login_required(login_url='/login')
@role_required(User.ADMIN)
def editdrivers(request):

    drivers = Driver.objects.all()


    obj_drivers = []
    for driver in drivers:
        obj_driver = dict()
        obj_driver['name'] = driver.name
        obj_driver['id'] = driver.id
        obj_driver['startdate'] = driver.startdate
        obj_driver['car'] = driver.car
        obj_driver['plq'] = driver.plq
        obj_driver['services'] = show_manytomany(driver.services)
        obj_drivers.append(obj_driver)


    return render(request,'main/editdrivers.html',{'drivers':drivers})


