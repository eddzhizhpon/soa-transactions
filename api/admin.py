from django.contrib import admin

from . models import User, Account

from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# Register your models here.
@admin.register(get_user_model())
class UserAdmin(UserAdmin):
    pass
# admin.site.register(User)

admin.site.register(Account)