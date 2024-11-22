from django.contrib import admin
from .models import Post
from django.contrib.auth.models import Group 

# Register your models here.
admin.site.register(Post)
admin.site.unregister(Group)
admin.site.site_header='Myblog Administration'
admin.site.site_title='Myblog'