from bookshelf.models import Book

# Retrieve the book we just created
book = Book.objects.get(title="1984")

book.title           # '1984'
book.author          # 'George Orwell'
book.publication_year  # 1949

# Expected output:
# '1984'
# 'George Orwell'
# 1949
