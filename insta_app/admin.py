from django.contrib import admin

# Register your models here.
from .models import Profile,Image,Comments

admin.site.register(Profile)
admin.site.register(Comments)
admin.site.register(Image)