from django.contrib import admin
from user.models import UserAccount, Reader, Publisher


admin.site.register(UserAccount)
admin.site.register(Reader)
admin.site.register(Publisher)
