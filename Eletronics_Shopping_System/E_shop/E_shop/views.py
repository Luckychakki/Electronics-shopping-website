import json
import logging

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect, get_object_or_404
from django.http import JsonResponse
from store_app.models import Product,Categories,Filter_Price,Color,Brand,Contact_us,Order,OrderItem
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.utils.crypto import get_random_string
from django.contrib.auth import update_session_auth_hash
def BASE(request):
    return render(request,'Main/base.html')


def HOME(request):
    product = Product.objects.filter(status='Publish')

    context = {
        'product':product,
    }
    return render(request,'Main/index.html',context)


def PRODUCT(request):

    categories = Categories.objects.all()
    filter_price = Filter_Price.objects.all()
    color = Color.objects.all()
    brand = Brand.objects.all()

    CATID = request.GET.get('categories')
    PRICE_FILTER_ID = request.GET.get('filter_price')
    COLORID = request.GET.get('color')
    BRANDID = request.GET.get('brand')
    ATOZID = request.GET.get('ATOZ')
    ZTOAID = request.GET.get('ZTOA')
    PRICE_LOWTOHIGHID = request.GET.get('PRICE_LOWTOHIGH')
    PRICE_HIGHTOLOWID = request.GET.get('PRICE_HIGHTOLOW')
    NEW_PRODUCTID = request.GET.get('NEW_PRODUCT')
    OLD_PRODUCTID = request.GET.get('OLD_PRODUCT')
    if CATID:
        product = Product.objects.filter(categories=CATID)
    elif PRICE_FILTER_ID :
        product = Product.objects.filter(filter_price=PRICE_FILTER_ID,status='Publish')
    elif COLORID:
        product = Product.objects.filter(color=COLORID, status='Publish')
    elif BRANDID:
        product = Product.objects.filter(brand=BRANDID, status='Publish')
    elif ATOZID:
        product = Product.objects.filter(status='Publish').order_by('name')
    elif ZTOAID:
        product = Product.objects.filter(status='Publish').order_by('-name')
    elif PRICE_LOWTOHIGHID:
        product = Product.objects.filter(status='Publish').order_by('price')
    elif PRICE_HIGHTOLOWID:
        product = Product.objects.filter(status='Publish').order_by('-price')
    elif NEW_PRODUCTID:
        product = Product.objects.filter(status='Publish',condition='New').order_by('-id')
    elif OLD_PRODUCTID:
        product = Product.objects.filter(status='Publish',condition='Old').order_by('-id')
    else:
        product = Product.objects.filter(status='Publish').order_by('-id')
    context = {
        'product': product,
        'categories':categories,
        'filter_price':filter_price,
        'color':color,
        'brand':brand
    }
    return render(request,'Main/product.html',context)


def SEARCH(request):
    query = request.GET.get('query')
    product = Product.objects.filter(name__icontains=query)
    context = {
        'product':product
    }
    return render(request,'Main/search.html',context)


def PRODUCT_DETAIL_PAGE(request,id):
    prod = Product.objects.filter(id=id).first()
    context = {
        'prod':prod
    }
    return render(request,"Main/product_single.html",context)


def Contact_Page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact_us(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )
        subject = subject
        message = message
        email_from = settings.EMAIL_HOST_USER
        try:
            send_mail(subject,message,email_from,['brewhaven3@gmail.com'])
            contact.save()
            return redirect('home')
        except:
             return redirect('contact')

    return render(request,'Main/contact.html')



def HandleRegister(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        customer = User.objects.create_user(username,email,pass1)
        customer.first_name = first_name
        customer.last_name = last_name
        customer.save()
        return redirect('home')
    return render(request,'Registration/auth.html')


def HandleLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('login')

    return render(request,'Registration/auth.html')



def reset_password(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        # Validate password confirmation
        if new_password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('reset_password')

        try:
            user = User.objects.get(username=username)
            user.set_password(new_password)
            user.save()
            messages.success(request, "Your password has been reset successfully.")
            return redirect('reset_password')  # Redirect to the login page after success
        except User.DoesNotExist:
            messages.error(request, "No user found with that username.")
            return redirect('reset_password')

    return render(request, 'Registration/ResetPassword.html')



def HandleLogout(request):
    logout(request)
    return redirect('home')
    #return render(request,'Main/index.html')





@login_required(login_url="/login/")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required(login_url="/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")




def cart_detail(request):
    return render(request, 'Cart/cart_details.html')


def Check_out(request):
    return render(request,'Cart/checkout.html')


def PLACE_ORDER(request):
    if request.method == 'POST':
        uid = request.session.get('_auth_user_id')
        user = User.objects.get(id=uid)
        cart = request.session.get('cart', {})
        #print(cart)
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        country = request.POST.get('country')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        postcode = request.POST.get('postcode')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        amount = request.POST.get('amount')
        #print(amount)

        order = Order(
            user = user,
            firstname = firstname,
            lastname = lastname,
            country = country,
            city = city,
            address = address,
            state = state,
            postcode = postcode,
            phone = phone,
            email = email,
            amount = amount
        )
        order.save()
        for i in cart:
            a = (int(cart[i]['price']))
            b = cart[i]['quantity']
            #print(type(a))
            #print(type(b))
            total = a * b
            #print(total)
            item = OrderItem(
                user = user,
                order = order,
                product = cart[i]['name'],
                image = cart[i]['image'],
                quantity = cart[i]['quantity'],
                price = cart[i]['price'],
                total = total
            )
            item.save()
            context = {
                'first_name': request.session.get('first-name', 'Not Provided'),
                'last_name': request.session.get('last-name', 'Not Provided'),
                'address': request.session.get('address', 'Not Provided'),
                'country': request.session.get('country', 'Not Provided'),
                'city': request.session.get('city', 'Not Provided'),
                'state': request.session.get('state', 'Not Provided'),
                'postcode': request.session.get('postcode', 'Not Provided'),
                'phone': request.session.get('phone', 'Not Provided'),
                'email': request.session.get('email', 'Not Provided'),
            }
            # Add logging to check if the view is being called
        logging.debug("Rendering placeorder page with context: %s", context)
        #print(firstname,lastname,country,address,city,state,postcode,phone,email,order_id,payment)
        return render(request,'Cart/placeorder.html',context)

def success(request):
    return render(request,'Cart/thankyou.html')


def Your_Order(request):
    uid = request.session.get('_auth_user_id')
    user = User.objects.get(id=uid)
    order = OrderItem.objects.filter(user = user)
    context = {
        'order' : order,
    }
    return render(request,"Main/your_order.html",context)


def ACCOUNT(request):
    username = request.GET.get('username')
    email = request.GET.get('email')
    return render(request,'Registration/account.html', {'username': username, 'email': email})


def PRODUCTDUP(request):

    categories = Categories.objects.all()
    filter_price = Filter_Price.objects.all()
    color = Color.objects.all()
    brand = Brand.objects.all()

    CATID = request.GET.get('categories')
    PRICE_FILTER_ID = request.GET.get('filter_price')
    COLORID = request.GET.get('color')
    BRANDID = request.GET.get('brand')
    ATOZID = request.GET.get('ATOZ')
    ZTOAID = request.GET.get('ZTOA')
    PRICE_LOWTOHIGHID = request.GET.get('PRICE_LOWTOHIGH')
    PRICE_HIGHTOLOWID = request.GET.get('PRICE_HIGHTOLOW')
    NEW_PRODUCTID = request.GET.get('NEW_PRODUCT')
    OLD_PRODUCTID = request.GET.get('OLD_PRODUCT')
    if CATID:
        product = Product.objects.filter(categories=CATID)
    elif PRICE_FILTER_ID :
        product = Product.objects.filter(filter_price=PRICE_FILTER_ID,status='Publish')
    elif COLORID:
        product = Product.objects.filter(color=COLORID, status='Publish')
    elif BRANDID:
        product = Product.objects.filter(brand=BRANDID, status='Publish')
    elif ATOZID:
        product = Product.objects.filter(status='Publish').order_by('name')
    elif ZTOAID:
        product = Product.objects.filter(status='Publish').order_by('-name')
    elif PRICE_LOWTOHIGHID:
        product = Product.objects.filter(status='Publish').order_by('price')
    elif PRICE_HIGHTOLOWID:
        product = Product.objects.filter(status='Publish').order_by('-price')
    elif NEW_PRODUCTID:
        product = Product.objects.filter(status='Publish',condition='New').order_by('-id')
    elif OLD_PRODUCTID:
        product = Product.objects.filter(status='Publish',condition='Old').order_by('-id')
    else:
        product = Product.objects.filter(status='Publish').order_by('-id')
    context = {
        'product': product,
        'categories':categories,
        'filter_price':filter_price,
        'color':color,
        'brand':brand
    }
    return render(request,'Main/productduplicate.html',context)



def save_order_data(request):
    if request.method == 'POST':
        # Clear the previous session data to prevent old data from persisting
        request.session.flush()  # This will clear all session data
        data = json.loads(request.body)
        request.session['first-name'] = data.get('first-name')
        request.session['last-name'] = data.get('last-name')
        request.session['address'] = data.get('address')
        request.session['country'] = data.get('country')
        request.session['city'] = data.get('city')
        request.session['state'] = data.get('state')
        request.session['postcode'] = data.get('postcode')
        request.session['phone'] = data.get('phone')
        request.session['email'] = data.get('email')
        return JsonResponse({'status': 'success'})