from django.contrib import admin
from .models import Category, Product, ProductGallery


class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1
    readonly_fields = ("image_compressed",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "date_created", "date_modified")
    search_fields = ("title",)
    list_filter = ("date_created", "date_modified")
    readonly_fields = ("date_created", "date_modified", "slug")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "formatted_base_price",
        "date_created",
        "date_modified",
    )
    search_fields = ("title", "description", "meta_key")
    list_filter = ("date_created", "date_modified")
    readonly_fields = ("date_created", "date_modified", "slug")
    inlines = [ProductGalleryInline]

    def formatted_base_price(self, obj):
        return f"Rp {obj.base_price:,.2f}".replace(",", ".")

    formatted_base_price.short_description = "Base Price"

    formatted_base_price.short_description = "Base Price"


@admin.register(ProductGallery)
class ProductGalleryAdmin(admin.ModelAdmin):
    list_display = ("product", "image", "image_compressed")
    search_fields = ("product__title",)
    readonly_fields = ("image_compressed",)
    list_filter = ("product",)
