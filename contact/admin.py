from django.contrib import admin
from contact import models

# Register your models here.
# Registar os models, e fazer configurações adicionais na area admim
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'frist_name',
        'last_name',
        'email',
        'created_date',
        'show',
    )
    ordering = '-id',
    list_filter  = 'created_date',
    search_fields = (
        'id',
        'frist_name',
        'last_name',
    ) 
    list_per_page = 50
    list_max_show_all = 100
    list_editable = 'show',

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = 'id',