from django.contrib import admin

# Register your models here.
from truck_app.models import Truck, Comment, Like


class TruckAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'owner',)
    list_filter = ('make', 'model', 'owner',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('truck', 'text', 'owner',)
    list_filter = ('truck', 'owner',)


class LikeAdmin(admin.ModelAdmin):
    list_display = ('truck', 'owner',)
    list_filter = ('truck', 'owner',)


admin.site.register(Like, LikeAdmin)
admin.site.register(Truck, TruckAdmin)
admin.site.register(Comment, CommentAdmin)
