from django.contrib import admin

# Register your models here.

from app.models import *

admin.site.register(User)

admin.site.register(Profile)

admin.site.register(Author)

admin.site.register(Book)

admin.site.register(Collection)

admin.site.register(Books)