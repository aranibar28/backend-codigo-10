from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views import generic
from core.models import Book

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello World!")

# Vista basada en function
def function_books(request):
        books = Book.objects.filter(author__contains="Otro") | Book.objects.filter(id__gt=0) 
        context = {
            "books": books,
            # "books": books.order_by("pub_date")
        }
        return render(request, "index.html", context)

# Vista basada en clases
class BooksView(View):
    def get(self, request):
        order_param = request.GET.get('order')
        books = Book.objects.filter()
        if order_param != None:
            books = books.order_by(order_param)

        context = {
            "books": books
        }
        return render(request, "index.html", context)

# Vista genérica
class BookListView(generic.ListView):
    model = Book
    queryset = Book.objects.order_by("pub_date")

""" Vistas de Detalle """

# Vista basada en function
def function_book(request, id):
    book = Book.objects.get(pk = id)
    context = {
        "book": book
    }
    return render(request, "detail.html", context)

# Vista basada en vista
class BookDetail(View):
    def get(self, request, id):
        book = Book.objects.get(pk = id)
        context = {
            "book": book
        }
        return render(request, "detail.html", context)

# Vista genérica
class BookDetailView(generic.DetailView):
    model = Book