from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Create router and register ViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Existing ListAPIView route
    path('books/', BookList.as_view(), name='book-list'),

    # Include all routes from the router for CRUD
    path('', include(router.urls)),
]