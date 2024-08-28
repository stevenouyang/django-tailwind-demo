from django.db import models
from autoslug import AutoSlugField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="title")
    image = models.ImageField(upload_to="images/category/")
    image_compressed = ImageSpecField(
        source="image",
        processors=[ResizeToFill(1000, 1000)],
        format="WebP",
        options={"quality": 90},
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["title"]


class Product(models.Model):
    title = models.CharField(max_length=245)
    slug = AutoSlugField(populate_from="title")
    category = models.ForeignKey(
        "Category",
        related_name="product_category",
        on_delete=models.CASCADE,
        default=None,
    )
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    meta_key = models.TextField(blank=True, null=True)
    meta_desc = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse("product:single_product", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["title"]


class ProductGallery(models.Model):
    product = models.ForeignKey(
        "Product", related_name="gallery_images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="images/product_gallery/")
    image_compressed = ImageSpecField(
        source="image",
        processors=[ResizeToFill(1000, 1000)],
        format="WebP",
        options={"quality": 90},
    )
    image_thumbnail = ImageSpecField(
        source="image",
        processors=[ResizeToFill(240, 240)],
        format="WebP",
        options={"quality": 80},
    )

    class Meta:
        verbose_name = "Product Gallery"
        verbose_name_plural = "Product Galleries"
        ordering = ["product"]
