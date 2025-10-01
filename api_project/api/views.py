from rest_framework import generics            # ✅ DRF generics import
from .models import Book                        # ✅ import your Book model
from .serializers import BookSerializer         # ✅ import the serializer

# Define the view
class BookList(generics.ListAPIView):           # ✅ class name and inheritance
    queryset = Book.objects.all()              # Get all Book objects
    serializer_class = BookSerializer   

    # New: ViewSet for full CRUD
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
# Create your views here.
