from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    url = models.URLField(unique=True)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    category = models.ManyToManyField("Category", related_name="books")
    #slug = models.SlugField(null=True)
    #genres =
    #favorited_by = models.ManyToManyField(User, related_name="favorite_books")
    
    def add_new(self):
        self.created_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, null=True, blank=True, unique=True)
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Category name=(self.name)>"

    def save(self):
        self.slug = slugify(self.name)
        super().save()

# class CustomUser(AbstractUser):
#     pass

#     def __str__(self):
#         return self.username