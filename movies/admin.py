from django.contrib import admin
from .models import *


# Register your models here.


class AdminGenre(admin.ModelAdmin):
    list_display = ('id', 'name')


class AdminMovie(admin.ModelAdmin):
    exclude = ('date_created',)
    list_display = ('title', 'genre', 'number_in_stock')


admin.site.register(Genre, AdminGenre)
admin.site.register(Movie, AdminMovie)

