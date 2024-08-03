from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from online_shop.form import OrderForm
from online_shop.models import Product, Order


# Create your views here.

def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'online_shop/home.html', context)


def product_detail(request, id):
    product = Product.objects.get(pk=id)
    products = Product.objects.exclude(pk=id)
    context = {
        'products': products,
        'product': product,
    }
    return render(request, 'online_shop/detail.html', context)


def add_order(request, slugs):
    product = get_object_or_404(Product, slug=slugs)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            quantity = int(request.POST.get('quantity', 0))
            if quantity <= product.quantity:
                product.quantity -= quantity
                product.save()

                order = form.save(commit=False)
                order.product = product
                order.save()

                messages.success(request, 'Buyurtma muvaffaqiyatli yaratildi 🤗🎉')
                return redirect('details', slugs)

            else:
                messages.error(request, "Iltimos, kamroq miqdorda buyurtma qiling 😐❗️")
        else:
            messages.error(request, "Forma noto'g'ri to'ldirilgan😕 ❗️")

    else:
        form = OrderForm()

    context = {
        'form': form,
        'product': product
    }

    return render(request, 'online_shop/detail.html', context)


###
from django.shortcuts import render, get_object_or_404, redirect
from online_shop.models import Product
from online_shop.form import ProductForm


# Create
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'online_shop/product_form.html', {'form': form})


# Read (List)
def product_list(request):
    products = Product.objects.all()
    return render(request, 'online_shop/product_list.html', {'products': products})


# Update
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'online_shop/product_form.html', {'form': form})


# Delete
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'online_shop/product_confirm_delete.html', {'product': product})

