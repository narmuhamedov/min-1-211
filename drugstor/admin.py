from django.contrib import admin
from drugstor.models import Customer, Tag, ProductForMedicine, Order

admin.site.register(Customer)
admin.site.register(Tag)
admin.site.register(ProductForMedicine)
admin.site.register(Order)