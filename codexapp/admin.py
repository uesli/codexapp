from django.contrib import admin
from codexapp.models import Category
from .models import Information

class InformationAdmin(admin.ModelAdmin):
    # cria uma lista com as colunas que seram exbibidas
    list_display = ["__unicode__", "category", "creation_date", "updated"]
    search_fields = ('title',)
    
    class Meta:
        model = Information

# Register your models here.  
admin.site.register(Category)
admin.site.register(Information, InformationAdmin)
