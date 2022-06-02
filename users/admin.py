from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


# class AccountInLine (admin.StackedInline):
# 	model = Profile
# 	can_delete = False

# class CustomAdmin (UserAdmin):
# 	inlines = (AccountInLine, )

# # Register your models here.

# admin.site.unregister(User)
# admin.site.register (User, CustomAdmin)
# admin.site.register(Profile)

admin.site.register(Profile)
