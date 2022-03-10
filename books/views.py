from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Book, Category
from .forms import BookForm

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect("list_books")
    return render(request, "books/home.html")

@login_required
def list_books(request):
    books = Book.objects.all().order_by("-created_date")
    categorys = Category.objects.all()
    return render(request, "books/list_books.html", {"books": books, "categorys": categorys})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm()
    return render(request, "books/book_detail.html", {"book": book, "form": form})

def check_admin_user(user):
    return user.is_staff

def show_category(request, slug):
    # albums = Album.objects.filter(genres__slug=slug)
    # I could do this ☝️ but...
    # even better to get all the albums associated with a genre:
    category = get_object_or_404(Category, slug=slug)
    books = category.books.all()

    return render(request, "books/category.html", {"category": category, "books": books})

@login_required
@user_passes_test(check_admin_user)
def add_book(request):
    if request.method == "POST":
        form = BookForm(data=request.POST)
        if form.is_valid():
            album = form.save()

            return redirect("book_detail", pk=album.pk)
    else:
        form = BookForm()

    return render(request, "books/add_book.html", {"form": form})

def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "GET":
        book = BookForm(instance=book)
    else:
        form = BookForm(data=request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("list_books")

    return render(request, "books/edit_book.html", {"form": form, "books": book})


def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.delete()
        return redirect("list_albums")

    return render(request, "books/delete_book.html", {"book": book})















# @login_required
# def add_favorite(request, book_pk):
#     #when we create a M2M relationship we need TWO instances 
#     #Here we need the book instance/object AND the user object/instance
#     book = get_object_or_404(Book, pk=book_pk)
#     user = request.user
#     user.favorite_books.add(book)
#     return render()


# def show_genre(request, slug):
#     genre = get_objects_or_404(Genre, slug=slug)
#     books = genre.books.all()
    
#     return render(request, "books/show_genre.html",{"genre": genre, "books": books})
    
    