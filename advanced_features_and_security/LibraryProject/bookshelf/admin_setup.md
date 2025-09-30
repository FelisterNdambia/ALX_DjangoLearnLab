# Django Admin Setup for Bookshelf App

## Objective
Gain practical experience with the Django admin interface by configuring the admin to manage the `Book` model. This documentation outlines the steps to register the model and customize the admin interface.

---

## Steps

### 1. Register the Book Model

Edit `bookshelf/admin.py`:

```python
from django.contrib import admin
from .models import Book

# Register Book with basic admin
# admin.site.register(Book)