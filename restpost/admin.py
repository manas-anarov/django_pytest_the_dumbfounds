from django.contrib import admin
from restpost.models import Post
from restpost.models import Category

admin.site.register(Post)
admin.site.register(Category)