from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Category, Product, Order, OrderItem, EventInquiry
from .forms import EventInquiryForm, ContactForm
from django.contrib import messages
from django.db.models import Sum

def home(request):

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Your message has been sent! We will get back to you soon.')
            return redirect('home')
    else:
        contact_form = ContactForm()

    categories = Category.objects.all()
    featured_products = Product.objects.filter(available=True).order_by('?')[:6]
    return render(request, 'store/home.html', {'categories': categories, 'featured_products': featured_products, 'contact_form': contact_form})

def products(request):
    categories = Category.objects.all()
    category_id = request.GET.get('category')
    if category_id:
        products = Product.objects.filter(category_id=category_id, available=True)
    else:
        products = Product.objects.filter(available=True)
    return render(request, 'store/products.html', {'products': products, 'categories': categories})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/product_detail.html', {'product': product})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'store/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def cart(request):
    cart_items = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart_items.keys())
    cart_details = []
    total_price = 0
    for product in products:
        quantity = cart_items[str(product.id)]
        subtotal = product.price * quantity
        total_price += subtotal
        cart_details.append({'product': product, 'quantity': quantity, 'subtotal': subtotal})
    return render(request, 'store/cart.html', {'cart_details': cart_details, 'total_price': total_price})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if product.stock <= 0:
        messages.error(request, f"{product.name} is out of stock.")
        return redirect('products')
    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart
    return redirect('cart')

@login_required
def checkout(request):
    if request.method == 'POST':
        address = request.POST.get('delivery_address')
        cart = request.session.get('cart', {})
        if not cart:
            return redirect('cart')
        total_price = sum(Product.objects.get(id=int(pid)).price * qty for pid, qty in cart.items())
        order = Order.objects.create(user=request.user, total_price=total_price, delivery_address=address)
        for product_id, quantity in cart.items():
            product = Product.objects.get(id=int(product_id))
            OrderItem.objects.create(order=order, product=product, quantity=quantity, price=product.price)
        request.session['cart'] = {}
        return redirect('order_confirmation', order_id=order.id)
    return render(request, 'store/checkout.html')

def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'store/order_confirmation.html', {'order': order})

@login_required
def event_inquiry(request):
    if request.method == 'POST':
        form = EventInquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.user = request.user
            inquiry.save()
            return redirect('home')
    else:
        form = EventInquiryForm()
    return render(request, 'store/event_inquiry.html', {'form': form})

def about(request):
    return render(request, 'store/about.html')