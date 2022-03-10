from django.contrib import admin
from .models import User, Book, Category

# Register your models here.
admin.site.register(User)
admin.site.register(Book)
admin.site.register(Category)