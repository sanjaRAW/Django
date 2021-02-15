import profile

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .filters import ProductFilter
from .forms import *
from .tokens import account_activation_token


def products_page(request):
    products = Products.objects.all()
    filter = ProductFilter(request.GET,queryset=products)
    products = filter.qs
    return render(request, 'products/products.html', {"products": products, 'filter':filter})



def order_page(request, product_id):
    try:
        profile = Profile.objects.get(user=request.user)
        product = Products.objects.get(id=product_id)
        total_price = 0
        discount_price = 0
        sale_amount = profile.sale_amount * 0.005
        form = OrderForm(initial={'product': product, 'user': request.user})
        if request.method == 'POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                if 20 < profile.order_count < 40:
                    profile.sale_amount = 0.1
                    total_price = (product.price - product.price * profile.sale_amount) * form.cleaned_data['quantity']
                elif 40 < profile.order_count < 60:
                    profile.sale_amount = 0.2
                    total_price = (product.price - product.price * profile.sale_amount) * form.cleaned_data['quantity']
                if form.cleaned_data['payment_method'] == 'wallet':
                    if profile.wallet >= total_price:
                        profile.wallet -= total_price
                        return HttpResponse('sps za pokupku')
                    else:
                        return HttpResponse('not enough munny')
                else:
                    profile.order_count += 1
                    profile.save()
                form.save()


        return render(request, 'products/order.html', {'form': form, 'total_price': total_price , 'discount_price': discount_price})
    except Products.DoesNotExist:
        return HttpResponse('Not found!')


def reg_page(request):
    register = SignUpform()
    if request.method == 'POST':
        register = SignUpform(request.POST)
        if register.is_valid():
            user = register.save(commit=False)
            user.is_active = True
            user.save()
            mail_subject = 'Activate!'
            current_site = get_current_site(request)
            to = register.cleaned_data.get('email')
            message = render_to_string('user_dir/activate.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            email = EmailMessage(mail_subject,message,to=[to])
            email.send()
            EmailMessage('lal','kaka',to=['maximneveraa@gmail.com',]).send()

            Profile.objects.create(user=user)
            return HttpResponse('Please confirm your email address to complete the registration')
    return render(request, 'user_dir/registerplaceholder.html', {'register': register})


def product_list(request, user_id):
    user = User.objects.get(id=user_id)
    orders = user.order_set.all()
    context = {'user': user, 'orders': orders}
    return render(request, 'products/userlist.html', context)


def about_us(request):
    paragr = About_us.objects.all()
    return render(request, 'products/abus.html', {'paragr': paragr})


def contacts_page(request):
    contact = Contacts.objects.all()
    return render(request, 'products/contacts.html', {'contacts': contact})


def update_order(request, order_id):
    order = Order.objects.get(id=order_id)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
        return redirect('products')
    return render(request, 'products/order.html', {'form': form})


def delete_order(request, order_id):
    order = Order.objects.get(id=order_id)
    order.delete()
    return redirect('products')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect('products')
    return render(request, 'products/login.html')


def logout_page(request):
    logout(request)
    return redirect('/')

def account_settings(request):
    try:
        user = request.user.profile
        order_user = request.user
        orders = order_user.order_set.all()
        form = ProfileForm(instance=user)
        if request.method == 'POST':
            form = ProfileForm(request.POST,request.FILES, instance=user)
            if form.is_valid():
                form.save()
        context = {'form': form, 'orders':orders}
        return render(request,'user_dir/profile.html',context)
    except AttributeError:
        return redirect('login')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('products')
    else:
        return HttpResponse('Activation link is invalid!')