from django.contrib import admin


# Register your models here.
from truck_auth.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)


admin.site.register(UserProfile, UserProfileAdmin)
