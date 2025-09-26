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
     