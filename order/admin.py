from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'email', 'paid', 'created', 'updated']
    list_filter = ['paid', 'updated', 'created']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
# Register your models here.
