try:
    from functools import wraps
except:
    from django.utils.functional import wraps

from django.shortcuts import render
from django.template import RequestContext
from django.http import Http404
from django.http import HttpResponseForbidden


from main.models import User

def role_required(*roles):
    """
    Check specified role(s) and return a 403
    if user doesn't have permission to view
    based alot on: github.com/mzupan/django-decorators/blob/master/auth.py
    and: djangofoo.com/253/writing-django-decorators
    """
    def check_role(user):   
        print(user)
        return user.role in roles
        
    def decorator(func):
        def inner_decorator(request,*args, **kwargs):
            print(request.user.id)
            if check_role(User.objects.filter(id=request.user.id).first()):
                return func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden()
        return wraps(func)(inner_decorator)
    return decorator

def show_manytomany(queryset):
    str = ""
    for i in queryset:
        str += f'{str(i)}, '
    return str