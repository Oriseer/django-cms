from django.contrib import admin
from .models import Client, ClientFiles
# Register your models here.



class FeedFileInline(admin.TabularInline):
    model = ClientFiles


class FeedAdmin(admin.ModelAdmin):
    inlines = [
        FeedFileInline,
    ]
admin.site.register(Client, FeedAdmin)
