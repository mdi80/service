import json
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from main.models import Driver, User
from django.conf import settings
from django.urls import reverse
from django.forms import ModelForm
from django import forms

from utils import role_required

class DriverForm(ModelForm):
    
    class Meta:
        model = Driver
        fields = ['username','password','first_name','last_name','car','plq']
        labels = {'username' : "نام کاربری",'password':"رمز عبور",'first_name':"نام",'last_name':"نام خانوادگی",'car':"خودرو",'plq':"پلاک"}
        widgets = {'password': forms.PasswordInput() }


@login_required(login_url='/login')
@role_required(User.ADMIN)
def add(request):

    form = DriverForm(request.POST or None ,request.FILES or None)

    form.instance.role = User.DRIVER
    if form.is_valid():
        form.save()
        return redirect('/edit-drivers')
    # errors = form.errors.keys()
    # errors_fa = []
    # for err in errors:
    #     if(form.errors.get_json_data(err)[err][0]['message'] == 'A user with that username already exists.'):
    #         errors_fa.append((DriverForm.Meta.labels[err] ,'نام کاربری وارد شده قبلا استفاده شده است.'))
    #         continue
    #     errors_fa.append({DriverForm.Meta.labels[err] : f'اطلاعات فیلد \'{DriverForm.Meta.labels[err]}\' نامعتبر است.'})

    return render(request,"driver/add.html",{'form' : form})


@login_required(login_url='/login')
@role_required(User.ADMIN)
def edit(request,id):
    # driver = Driver.objects.get(pk=id)

    # if request.method == 'POST':
    #     form = DriverForm(request.POST or None,instance=driver)

    #     if form.is_valid():
    #         form.save()
    #         return redirect('/edit-drivers')

    # else:
    #     print(driver.first_name)
    #     form = DriverForm(instance=driver)


    obj = Driver.objects.get(id=id)
    if request.method == 'GET':
        form = DriverForm(instance=obj)
        print(form.errors.as_json())

    else:  # POST
        form = DriverForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/edit-drivers')

    return render(request,"driver/edit.html",{'form' : form})

    # errors = form.errors.keys()
    # errors_fa = []
    # for err in errors:
    #     if(form.errors.get_json_data(err)[err][0]['message'] == 'A user with that username already exists.'):
    #         errors_fa.append((DriverForm.Meta.labels[err] ,'نام کاربری وارد شده قبلا استفاده شده است.'))
    #         continue
    #     errors_fa.append({DriverForm.Meta.labels[err] : f'اطلاعات فیلد \'{DriverForm.Meta.labels[err]}\' نامعتبر است.'})

    return render(request,"driver/add.html",{'form' : form})



    return redirect('/edit-drivers')


@login_required(login_url='/login')
@role_required(User.ADMIN)
def delete(request):

    if request.method == 'POST':
        print(request.POST)
        id = request.POST['id']
        print(f'id : {id}')
        Driver.objects.filter(id=id).first().delete()

    return redirect('/edit-drivers')

