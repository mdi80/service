from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ADMIN = 1
    DRIVER = 2
    PARENT =3
    
    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (DRIVER, 'Driver'),
        (PARENT, 'Parent'),
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
    

class Driver(User):
    car = models.TextField(max_length=100)
    plq = models.TextField(max_length=9)

class Parent(User):
    students = models.ManyToManyField('main.Student')

class Student(models.Model):
    name = models.TextField(max_length=100)

class Service(models.Model):
    time = models.DateTimeField()
    school = models.TextField(max_length=50)
    studens = models.ManyToManyField('main.Student')
    driver = models.ManyToManyField('main.Driver')

    def __str__(self) -> str:
        return f'{self.school} ({self.time})'
