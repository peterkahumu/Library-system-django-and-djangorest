from django.contrib import admin
from .models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'isbn']
    search_fields = ['id', 'isbn', 'isbn', 'author']
    list_filter = ['author', ]