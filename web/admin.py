from django.contrib import admin
from web import models

to_register=[models.Order]
admin.site.register(to_register)

