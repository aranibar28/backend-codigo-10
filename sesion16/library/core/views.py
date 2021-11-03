from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views import generic
from core.models import Book
import random 

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello World!")

# Vista basada en function
def function_books(self, request):
        books = Book.objects.all()
        context = {
            "books": books,
        }
        return render(request, "index.html", context)

# Vista basada en clases
class BooksView(View):
    def get(self, request):
        books = Book.objects.all()
        context = {
            "books": random.sample(list(books.order_by("editorial")),1),
        }
        return render(request, "index.html", context)

# Vista generica
class BookListView(generic.ListView):
    model = Book
    queryset = Book.objects.order_by("pub_date")

def function_book(request, id):
    books = Book.objects.get(pk = id)
    context = {
        "books": books
    }
    return render(request, "detail.html", context)