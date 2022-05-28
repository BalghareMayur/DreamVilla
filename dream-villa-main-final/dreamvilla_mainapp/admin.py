from django.contrib import admin

# Register your models here.
from .models import User
from .models import sell_property
from .models import sell_property1
admin.site.register(User)
admin.site.register(sell_property)
admin.site.register(sell_property1)