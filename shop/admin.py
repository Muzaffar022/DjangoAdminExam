from django.contrib import admin
from shop.models import Sale, Company, Product


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("title", "phone_number", "address")


@admin.register(Product)
class AdminProducts(admin.ModelAdmin):
    list_display = ("title", "price", "quantity", "company", "all_qty")

    def all_qty(self, obj):
        return f"{obj.quantity * obj.price}"

    def has_delete_permission(self, request, obj=None):
        if obj is not None and obj.quantity > 0:
            return False
        return super().has_delete_permission(request, obj)


@admin.register(Sale)
class Sales(admin.ModelAdmin):
    list_display = ("consumer", "quantity", "product", "data")

    def save_model(self, request, obj, form, change):
        if obj.quantity > obj.product.quantity:
            raise ValueError("Not enough to sold this product")
        obj.product.quantity -= obj.quantity
        obj.product.save()
        super().save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
