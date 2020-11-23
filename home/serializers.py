from .models import *
from rest_framework import serializers
from .views import *

class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id','title','price','discounted_price','image','slug','stock','labels','special_offer']

class BannerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ['id','title','image','discount']