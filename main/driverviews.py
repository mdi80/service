from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from main.models import Driver, User
from django.conf import settings
from django.urls import reverse
from django.forms import ModelForm

from utils import role_required

class DriverForm(ModelForm):
    
    class Meta:
        model = Driver
        fields = ['username','password','first_name','last_name','car','plq']
        labels = {'username' : "نام کاربری",'password':"رمز عبور",'first_name':"نام",'last_name':"نام خانوادگی",'car':"خودرو",'plq':"پلاک"}


@login_required(login_url='/login')
@role_required(User.ADMIN)
def add(request):

    form = DriverForm(request.POST or None ,request.FILES or None)

    print("test")
    form.instance.role = User.DRIVER
    if form.is_valid():
        form.save()
        return redirect('/edit-drivers')

    return render(request,"driver/add.html",{'form' : form})


@login_required(login_url='/login')
@role_required(User.ADMIN)
def edit(request,id):

    return redirect(reverse('edit-drivers'))


@login_required(login_url='/login')
@role_required(User.ADMIN)
def delete(request,id):

    print('delete')

    return redirect(reverse('edit-drivers'))

