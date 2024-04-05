from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from .models import *
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
# Create your views here.
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form':form}
    return render(request,'app/register.html', context )
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request,'user or password not correct!')
    context = {}
    return render(request,'app/login.html', context )
def logoutPage(request):
    logout(request)
    return redirect('login')
def home(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer = customer,complete= False)
        items = order.order_item_set.all()
        cartItems = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show"
    else:
        items = []
        order = {'get_cart_items':0,'get_cart_total':0}
        cartItems = order['get_cart_items']
        user_not_login = "show"
        user_login = "hidden"
    categories = Category.objects.filter(is_sub=False)
    active_category = request.GET.get('category','')
    products = Product.objects.all()
    context = {'categories':categories,'products': products, 'cartItems':cartItems,'user_not_login': user_not_login, 'user_login':user_login  }
    return render(request, "app/home.html",context)
def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer = customer,complete= False)
        items = order.order_item_set.all()
        cartItems = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show"
    else:
        items = []
        order = {'get_cart_items':0,'get_total':0}
        cartItems = order['get_cart_items']
        user_not_login = "show"
        user_login = "hidden"
    categories = Category.objects.filter(is_sub=False)
    active_category = request.GET.get('category','')
    context = {'categories':categories,'items':items, 'order':order, 'cartItems':cartItems,'user_not_login': user_not_login, 'user_login':user_login}
    return render(request, "app/cart.html",  context)
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer = customer,complete= False)
        items = order.order_item_set.all()
        cartItems = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show"
    else:
        items = []
        order = {'get_cart_items':0,'get_cart_total':0}
        cartItems = order['get_cart_items']
        user_not_login = "show"
        user_login = "hidden"
    categories = Category.objects.filter(is_sub=False)
    active_category = request.GET.get('category','')
    context = {'categories':categories,'items':items, 'order':order, 'cartItems':cartItems, 'user_not_login': user_not_login, 'user_login':user_login}
    return render(request, "app/checkout.html",  context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    customer = request.user
    product = Product.objects.get(id = productId)
    order, created = Order.objects.get_or_create(customer = customer,complete= False)
    order_item, created = Order_item.objects.get_or_create(order = order,product= product)
    if action == 'add':
        order_item.quantity += 1
    elif action =='remove':
        order_item.quantity -= 1
    order_item.save()
    if order_item.quantity <= 0 :
        order_item.delete()
    return JsonResponse('added', safe=False)

def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        keys = Product.objects.filter(name__contains = searched)
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer = customer,complete= False)
        items = order.order_item_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items':0,'get_cart_total':0}
        cartItems = order['get_cart_items']
    categories = Category.objects.filter(is_sub=False)
    active_category = request.GET.get('category','')
    products = Product.objects.all()
    return render(request, 'app/search.html', {'categories':categories,"searched":searched, 'keys':keys, 'products': products, 'cartItems':cartItems})

def category(request):
    categories = Category.objects.filter(is_sub=False)
    active_category = request.GET.get('category','')
    if active_category:
        products = Product.objects.filter(category__slug = active_category)
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer = customer,complete= False)
        items = order.order_item_set.all()
        cartItems = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show"
    else:
        items = []
        order = {'get_cart_items':0,'get_cart_total':0}
        cartItems = order['get_cart_items']
        user_not_login = "show"
        user_login = "hidden"
    context = {'categories':categories, 'products':products,'cartItems':cartItems, 'active_category':active_category,'user_not_login': user_not_login, 'user_login':user_login}
    return render(request, "app/category.html",  context)
        
def detail(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer = customer,complete= False)
        items = order.order_item_set.all()
        cartItems = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show"
    else:
        items = []
        order = {'get_cart_items':0,'get_total':0}
        cartItems = order['get_cart_items']
        user_not_login = "show"
        user_login = "hidden"
    id = request.GET.get('id','')
    products = Product.objects.filter(id=id)
    categories = Category.objects.filter(is_sub=False)
    active_category = request.GET.get('category','')
    context = {'categories':categories,'products': products,'items':items, 'order':order, 'cartItems':cartItems,'user_not_login': user_not_login, 'user_login':user_login}
    return render(request, "app/detail.html",  context)


def remove_from_cart(request, product_id):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        try:
            item = Order_item.objects.get(order=order, product__id=product_id)
            item.delete()
        except Order_item.DoesNotExist:
            pass  # Bỏ qua nếu không tìm thấy item
    return redirect('cart')