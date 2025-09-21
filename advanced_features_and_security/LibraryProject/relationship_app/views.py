from .models import Book, Author  # Import your models
from .models import UserProfile
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required


def list_books(request):
    """Function-based view to list all books"""
    books = Book.objects.all().select_related('author')
    return render(request, 'relationship_app/list_books.html', {
        'books': books
    })


class LibraryDetailView(DetailView):
    """Class-based view to display library details"""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_queryset(self):
        return Library.objects.prefetch_related('books__author')


# User Login View

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Change to your desired post-login view
            return redirect('relationship_app:book_list')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# User Logout View


@login_required
def logout_view(request):
    logout(request)
    return redirect('relationship_app:login')

# User Registration View


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Redirect after successful registration
            return redirect('relationship_app:book_list')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Example of a protected view


@login_required
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})
# relationship_app/views.py


# Check if the user is an Admin


def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'

# Check if the user is a Librarian


def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'

# Check if the user is a Member


def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
# relationship_app/views.py


@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        # Assuming you have a way to select authors
        author_id = request.POST.get('author')
        publication_date = request.POST.get('publication_date')

        if title and author_id and publication_date:
            # Fetch the author instance
            author = Author.objects.get(id=author_id)
            Book.objects.create(title=title, author=author,
                                publication_date=publication_date)
            # Redirect after saving
            return redirect('relationship_app:book_list')

    # Render an empty form or instructions
    return render(request, 'relationship_app/add_book.html')


@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        publication_date = request.POST.get('publication_date')

        if title and author_id and publication_date:
            author = Author.objects.get(id=author_id)
            book.title = title
            book.author = author
            book.publication_date = publication_date
            book.save()
            return redirect('relationship_app:book_list')

    return render(request, 'relationship_app/edit_book.html', {'book': book})


@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        book.delete()
        return redirect('relationship_app:book_list')

    return render(request, 'relationship_app/delete_book.html', {'book': book})
