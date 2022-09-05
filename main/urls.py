from django.urls import path

from . import views,driverviews


app_name = "main"

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('edit-drivers',views.editdrivers,name='edit-drivers'),
    path('edit-drivers/delete/<int:id>',driverviews.delete,name='delete-driver'),
    path('edit-drivers/edit/<int:id>',driverviews.edit,name='edit-driver'),
    path('edit-drivers/add',driverviews.add,name='add-driver'),
    path('edit-students',views.dashboard,name='edit-students'),
    path('add-service',views.dashboard,name='add-service'),
    path('services',views.dashboard,name='services'),

]


