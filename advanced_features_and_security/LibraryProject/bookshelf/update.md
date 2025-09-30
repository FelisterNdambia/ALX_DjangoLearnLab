# Retrieve and update the book's title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

book.title
# Expected output:
# 'Nineteen Eighty-Four'