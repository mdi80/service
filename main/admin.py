from django.contrib import admin

from main.models import User,Driver,Parent,Student,Service

# Register your models here.
admin.site.register(User)
admin.site.register(Driver)
admin.site.register(Parent)
admin.site.register(Student)
admin.site.register(Service)
