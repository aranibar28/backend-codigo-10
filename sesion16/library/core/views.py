from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from core.models import Book

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello World!")

class BooksView(View):
    def get(self, request):
        books = Book.objects.all()

        context = {
            "books": books,
        }

        return render(request, "index.html", context)
