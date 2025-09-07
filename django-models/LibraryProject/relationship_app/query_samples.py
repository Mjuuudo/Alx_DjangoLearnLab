from relationship_app.models import Author, Book, Library, Librarian

def sample_data():
    author = Author.objects.create(name="George Orwell")
    book1 = Book.objects.create(title="1984", author=author)
    book2 = Book.objects.create(title="Animal Farm", author=author)

    library = Library.objects.create(name="Central Library")
    library.books.add(book1, book2)

    Librarian.objects.create(name="Alice", library=library)

def queries():
    author_name = "George Orwell"
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    print(books_by_author)

    library_name = "Central Library"
    library = Library.objects.get(name=library_name)
    print(library.books.all())

    librarian = Librarian.objects.get(library=library)
    print(librarian)