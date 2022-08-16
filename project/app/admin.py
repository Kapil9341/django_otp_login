from django.contrib import admin
from .models import Student
from .models import User

# Register your models here.
admin.site.register(Student)
admin.site.register(User)