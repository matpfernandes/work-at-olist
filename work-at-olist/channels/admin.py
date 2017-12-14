from django.contrib import admin
from .models import Channel

class ChannelModelAdmin(admin.ModelAdmin):
    list_display = ('name','uuid')
    search_fields = ('name',)

admin.site.register(Channel, ChannelModelAdmin)
