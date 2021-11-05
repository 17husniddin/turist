from django.contrib import admin

from turist.models import Turist, Category

# Register your models here.

class TuristAdmin(admin.ModelAdmin):
    list_display = ('name', 'content')
    list_display_links = ('name',)
    search_fields = ('name', 'content')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('name',)
    search_fields = ('name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Turist, TuristAdmin)