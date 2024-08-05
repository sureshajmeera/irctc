from django.contrib import admin
from .models import Users
from .models import Trains

admin.site.register(Users)
admin.site.register(Trains)