from .models import ProductGallery


def set_main_images(products):
    for product in products:
        first_image = ProductGallery.objects.filter(product=product).first()
        product.main_image = first_image.image_thumbnail.url if first_image else None
