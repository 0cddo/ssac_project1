from django.contrib import admin

from consume.models import Consumption

# Register your models here.

class ConsumptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'buy_date', 'gender', 'age', 'product', 'total']

admin.site.register(Consumption, ConsumptionAdmin)