from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # columns in list view
    list_filter = ('publication_year',)                     # add filter sidebar
    search_fields = ('title', 'author')                    # enable search box

# Register your models here.
