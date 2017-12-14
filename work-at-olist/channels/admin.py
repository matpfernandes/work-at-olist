from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from channels.models import Channel, Category


class ChannelModelAdmin(admin.ModelAdmin):
    list_display = ('name','uuid')
    search_fields = ('name',)

class CategoryModelAdmin(MPTTModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    mptt_level_indent = 20

admin.site.register(Channel, ChannelModelAdmin)
admin.site.register(Category, CategoryModelAdmin)
