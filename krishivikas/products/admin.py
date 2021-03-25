from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import *


# Register your models here.
class CustomerAdmin(SummernoteModelAdmin,
                    admin.ModelAdmin):  # instead of ModelAdmin
    summernote_fields = "__all__"
    list_display = ["name", "city"]
    search_fields = ["name"]
    list_filter = ("city", )


class ProductCommentAdmin(SummernoteModelAdmin,
                          admin.ModelAdmin):  # instead of ModelAdmin
    summernote_fields = "__all__"
    list_display = ["author", "product"]
    search_fields = ["product"]
    list_filter = ("product", )


class VendorAdmin(SummernoteModelAdmin,
                  admin.ModelAdmin):  # instead of ModelAdmin
    summernote_fields = "__all__"
    list_display = ["name", "city"]
    search_fields = ["name"]
    list_filter = ("city", )


class ProductAdmin(SummernoteModelAdmin,
                   admin.ModelAdmin):  # instead of ModelAdmin
    summernote_fields = "__all__"
    list_display = ["name", "vendor", "category"]
    search_fields = ["name", "category", "vendor"]
    list_filter = (
        "category",
        "is_new",
        "vendor",
        "price",
    )


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(ProductComment, ProductCommentAdmin)
