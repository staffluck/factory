from django.contrib import admin

from .models import TradePoint, Employee, Visit

@admin.register(TradePoint)
class TradePointAdmin(admin.ModelAdmin):
    search_fields = ("title", )

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ("name", )

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    search_fields = ("tradepoint__title", "tradepoint__employee__name")
