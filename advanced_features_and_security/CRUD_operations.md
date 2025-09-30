# Create a new book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

book
# Expected output:
# <Book: 1984>

# Retrieve the book we just created
book = Book.objects.get(title="1984")

book.title           # '1984'
book.author          # 'George Orwell'
book.publication_year  # 1949

# Expected output:
# '1984'
# 'George Orwell'
# 1949

# Retrieve and update the book's title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

book.title
# Expected output:
# 'Nineteen Eighty-Four'

# Retrieve and delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
Book.objects.all()
# Expected output:
# <QuerySet []>
