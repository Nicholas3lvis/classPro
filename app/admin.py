from django.contrib import admin
from .models import Blog
from .models import Employ
# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','author','category','date')
    search_fields = ('title','content','category')
    list_filter = ('category','date')

@admin.register(Employ)
class EmployAdmin(admin.ModelAdmin):
    list_display = ('name','email','department')
    search_fields = ('name','email','department')
