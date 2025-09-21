# Delete Operation

```python
from bookshelf.models import Book

# Assuming you have a book instance already created or fetched:
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Verify deletion by checking all Book records:
print(Book.objects.all())  # Output: <QuerySet []>
```
