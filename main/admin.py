from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Post)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'description', 'adress',
                    'director', 'phone_number', 'image', 'video']
    prepopulated_fields = {'slug': ('title',)}
