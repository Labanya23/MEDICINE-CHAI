from django.contrib import admin
from . models import Product,Customer,Cart,Payment,OrderPlace

# Register your models here.



class ProductModelAdmin(admin.ModelAdmin):
    list_displayed = ['id','title','discounted_price','category','product_image']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','locality','city','state','zipcode']

admin.site.register(Product, ProductModelAdmin)

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']

@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','amount','bikaspay_order_id','bikaspay_payment_status','bikaspay_payment_status','bikas_payment_id','paid']

@admin.register(OrderPlace)
class OrderPlaceModelAdmin(admin.ModelAdmin):
    list_display=['id','user','customer','product','quantity','ordered_date','status','payment']


