from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import *

# Create your views here.
from django.views.generic.base import View


class BaseView(View):
    template_views = {}

class HomeView(BaseView):
    def get(self, request):
        # self.template_views['items'] = Item.objects.filter(front = True)
        self.template_views['items'] = Item.objects.all()
        self.template_views['categories'] = Category.objects.all()
        self.template_views['images'] = Image.objects.all()
        # self.template_views['subcategories'] = Subcategory.objects.all()
        self.template_views['sliders'] = Slider.objects.all()
        self.template_views['movers'] = Mover.objects.all()
        self.template_views['special_offer'] = Item.objects.filter(special_offer=True)
        self.template_views['feature_product'] = Item.objects.filter(feature_product=True)
        return render(request, 'index.html', self.template_views)

class ItemView(BaseView):
    def get(self,request):
        self.template_views['information'] = Information.objects.all()
        self.template_views['items'] = Item.objects.all()
        self.template_views['banners'] = Banner.objects.all()
        self.template_views['c_banners'] = C_Banner.objects.all()
        return render(request,'shop.html',self.template_views)

class SingleView(BaseView):
    def get(self,request,slug):
        self.template_views['view_items'] = Item.objects.filter(slug=slug)

        return render(request, 'single.html', self.template_views)

class SearchView(BaseView):
    def get(self, request):
        query = request.GET.get('Search', 'None')
        if not None:
            self.template_views['search_result'] = Item.objects.filter(title__icontains=query)
            self.template_views['search_for'] = query

        return render(request, 'search.html', self.template_views)

class AboutView(BaseView):
    def get(self, request):
        self.template_views['about'] = About.objects.all()
        return render(request, 'about.html', self.template_views)


def signup(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']

        if password == re_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,"The username is already taken")
                return redirect('home:signup')
            elif User.objects.filter(email = email).exists():
                messages.error(request, "The email is already taken")
                return redirect('home:signup')
            else:
                user = User.objects.create_user(

                    username = username,
                    email = email,
                    password = password,
                    first_name = first_name,
                    last_name = last_name

                )
                user.save()
                user = auth.authenticate(username=username, password=password)
                auth.login(request, user)
                messages.success(request, "Register successfull")
                return redirect('home:login')


                # return redirect('home:signup')
        else:
            messages.error(request, 'Password incorrect')
            return redirect('home:signup')

    return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request, "Password does not match")
            return redirect('home:login')

    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def checkout(request):
    return render(request,'checkout.html')

@login_required
# def cart(request):
#     views = {}
#     views['carts'] = Cart.objects.filter(checkout = False,user = request.user)
#     return render(request,'cart.html',views)

def cart(request):
    shopcart = Cart.objects.filter(checkout = False,user = request.user)
    carttotal = 0
    for rs in shopcart:
        carttotal += rs.quantity * rs.price
    context = {'shopcart': shopcart,
                'carttotal': carttotal
               }
    return render(request, 'cart.html', context)

@login_required
def add_to_cart(request):
    if request.method == 'POST':
        title = request.POST['title']
        slug = request.POST['slug']
        image = request.POST['image']
        price = request.POST['price']
        description = request.POST['description']
        if Cart.objects.filter(slug=slug).exists():
            quantity = Cart.objects.get(slug=slug).quantity
            Cart.objects.filter(slug=slug).update(quantity = quantity+1)
            return redirect('home:cart')
        else:
            my_cart = Cart.objects.create(
            user = request.user,
            slug = slug,
            title = title,
            image = image,
            description = description,
            price = price
            )
            my_cart.save()
            return redirect('home:cart')
    else:
        return redirect('/')

def delete_cart(request,slug):
    if Cart.objects.filter(slug=slug).exists():
        Cart.objects.filter(slug=slug).delete()
        messages.success(request, "Item is deleted")
        return redirect('home:cart')
    else:
        return redirect('home:cart')
        messages.error(request, "The item is not in your database")

class ContactView(BaseView):
    def get(self, request):
        views = {}
        views['information'] = Information.objects.all()
        return render(request, 'contact.html', views)






def contactus(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        telephone = request.POST['telephone']
        contact = Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
            telephone=telephone
        )
        contact.save()
        messages.success(request, 'The message is sent.')
        return redirect('home:contact')

def order(request):
    if request.method == "POST":
        full_name = request.POST['full_name']
        telephone = request.POST['telephone']
        landmark = request.POST['landmark']
        town = request.POST['town']
        address = request.POST['address']
        order_item = Order.objects.create(
            user=request.user,
            full_name=full_name,
            telephone=telephone,
            landmark=landmark,
            town=town,
            address=address
        )
        order_item.save()
        messages.success(request, 'Order Complete.')
        return redirect('home:checkout')




# For REST API
from .serializers import *
from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializers

class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializers

class ItemFilterListView(generics.ListAPIView):
    serializer_class = ItemSerializers
    queryset = Item.objects.all()

    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)

    filter_fields = ['id','title','price','discounted_price','stock','labels','special_offer']
    ordering_fields = ['id','title','price','labels']
    search_fields = ['title','description']





