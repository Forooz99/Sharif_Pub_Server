from django.contrib import admin
from .models import Journal,Category,Volume

admin.site.register(Journal)
admin.site.register(Category)
admin.site.register(Volume)