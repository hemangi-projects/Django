from django.contrib import admin
from profiles_api import models


admin.site.register(models.UserProfile)
#this tells django admin to register our user profile model with the admin site means accessible through the admin interface
# Register your models here.
