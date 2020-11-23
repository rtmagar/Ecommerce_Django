from django.conf import settings
from django.db import models
from django.urls import reverse

STATUS = (('active', 'active'),("", 'default'))
STOCK = (('In Stock', 'In Stock'),('Out of Stock', 'Out of Stock'))
LABELS = (('Hot', 'Hot'),('Sale','Sale'),('New', 'New'))

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)
    # image = models.ImageField(upload_to='media', blank=True)
    # s_image = models.ImageField(upload_to='media', blank=True)
    # front = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    slug = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

class Item(models.Model):
    title = models.CharField(max_length=300)
    price = models.IntegerField()
    discounted_price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='media')
    # image = models.TextField()
    description = models.TextField(blank=True)
    slug = models.CharField(max_length=300, unique=True)
    stock = models.CharField(max_length=100, choices=STOCK)
    labels = models.CharField(choices=LABELS,max_length=50, blank=True)
    special_offer = models.BooleanField(default=False)
    front = models.BooleanField(default=False)
    feature_product = models.BooleanField(default=False)


    def __str__(self):
        return self.title

    def specials_offers(self):
        return self.price - self.discounted_price

    def get_item_url(self):
        return reverse('home:product', kwargs={'slug': self.slug})

    def add_to_cart(self):
        return reverse('home:add_to_cart', kwargs={'slug': self.slug})


class Image(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.title


class Slider(models.Model):
    title = models.CharField(max_length=300)
    # image = models.TextField()
    image = models.ImageField(upload_to='media')
    rank = models.IntegerField()
    status = models.CharField(choices=STATUS,max_length=100,blank=True)
    upper_part = models.CharField(max_length=400, blank=True)
    lower_part = models.CharField(max_length=400, blank=True)

    def __str__(self):
        return self.title

class Mover(models.Model):
    title = models.CharField(max_length=300)
    # image = models.TextField()
    image = models.ImageField(upload_to='media')
    rank = models.IntegerField(default=0)
    status = models.CharField(choices=STATUS, max_length=100, blank=True)

    def __str__(self):
        return self.title

class Banner(models.Model):
    title = models.CharField(max_length=300)
    # image = models.TextField()
    image = models.ImageField(upload_to='media')
    discount = models.CharField(max_length=400, blank=True)

    def __str__(self):
        return self.title

class C_Banner(models.Model):
    title = models.CharField(max_length=300)
    # image = models.TextField()
    image = models.ImageField(upload_to='media')
    discount = models.CharField(max_length=400, blank=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=300)
    telephone = models.IntegerField()
    subject = models.TextField()
    message = models.TextField()
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.TextField()
    title = models.CharField(max_length=200, blank=True)
    image = models.TextField(blank=True)
    # image = models.ImageField(upload_to='media')
    description = models.TextField(blank=True)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)
    checkout = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def delete_cart(self):
        return reverse('home:delete_cart', kwargs={'slug':self.slug})

class Information(models.Model):
    address = models.CharField(max_length=500)
    # local = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)
    # timing = models.CharField(max_length=200)
    email = models.CharField(max_length=300)

    def __str__(self):
        return self.phone

class About(models.Model):
    title = models.CharField(max_length=200, blank=True)
    detail = models.TextField(blank=True)
    image = models.ImageField(upload_to='media')
    question = models.CharField(max_length=300)
    answer = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=300)
    telephone = models.IntegerField()
    landmark = models.TextField()
    town = models.TextField()
    address = models.TextField()

    def __str__(self):
        return self.user.username




