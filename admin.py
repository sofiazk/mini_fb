# file name: admin.py
from django.contrib import admin

#register models here

from .models import Quote, Person, Image
admin.site.register(Quote)
admin.site.register(Person)
admin.site.register(Quote)
