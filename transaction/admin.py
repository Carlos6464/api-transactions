from django.contrib import admin
from transaction.models import Category, Transacions

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'created_at')
    list_display_links = ('id','name',)
    list_per_page = 10
    search_fields = ('name',)

admin.site.register(Category, CategoryAdmin)

class TransacionsAdmin(admin.ModelAdmin):
    list_display = ('id','description', 'value', 'nature', 'created_at')
    list_display_links = ('id','description',)
    list_per_page = 10
    search_fields = ('description',)

admin.site.register(Transacions, TransacionsAdmin)