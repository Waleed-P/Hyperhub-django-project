from django.contrib import admin
from . models import *
admin.site.register(ProductModel)
admin.site.register(CategoryModel)
admin.site.register(AvailableOffers)
admin.site.register(GenderModel)
admin.site.register(ProfileModel)
admin.site.register(CartItem)
admin.site.register(InventoryModel)
admin.site.register(OrdersModel)
# Register your models here.
