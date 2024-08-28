from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Product, ProductGallery
from crm.models import UserForm
from .utils import set_main_images


def home_view(request):
    products = Product.objects.all()
    set_main_images(products)
    context = {
        "products": products,
    }
    return render(request, "pages/home.html", context)


def single_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    product_gallery = ProductGallery.objects.filter(product=product)
    recommended_products = Product.objects.exclude(id=product.id)[:4]
    set_main_images(recommended_products)
    context = {
        "product": product,
        "recommended_products": recommended_products,
        "product_gallery": product_gallery,
    }
    return render(request, "pages/single_product.html", context)


def htmx_form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        UserForm.objects.create(name=name, email=email, message=message)
        return render(request, "pages/htmx_response.html", {}, content_type="text/html")

    return render(request, "pages/htmx_form.html", {})