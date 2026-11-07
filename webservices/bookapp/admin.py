from django.contrib import admin
from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pageCount')
    search_fields = ('title', 'author')
    list_filter = ('pageCount', 'author')
    fields = ('title', 'author', 'pageCount')