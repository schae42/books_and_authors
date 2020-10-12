from django.shortcuts import render, redirect
from .models import Books, Authors
# Create your views here.

def index(request):
    context = {
        'books' : Books.objects.all()
    }
    return render(request, "index.html", context)

def add_book(request):
    new_book = Books.objects.create(title = request.POST['title'], desc = request.POST['desc'])
    return redirect('/')

def book_info(request, book_id):
    context = {
        'books' : Books.objects.get(id = book_id),
        'authors' : Books.objects.get(id = book_id).authors.all(),
        'all_authors' : Authors.objects.all(),
    }
    return render(request, "book_info.html", context)

def append_authors(request, book_id):
    option = Authors.objects.get(id = request.POST['select_author'])
    Books.objects.get(id = book_id).authors.add(option)
    return redirect(f'/books/{book_id}')

def authors(request):
    context = {
        'authors' : Authors.objects.all()
    }
    return render(request, "authors.html", context)

def add_author(request):

    new_author = Authors.objects.create(first_name = request.POST['fname'], last_name = request.POST['lname'], notes = request.POST['notes'])
    return redirect('/authors')

def author_info(request, author_id):
    context = {
        'authors' : Authors.objects.get(id = author_id),
        'books' : Authors.objects.get(id = author_id).books.all(),
        'all_books' : Books.objects.all(),
    }
    return render(request, "author_info.html", context)

def append_books(request, author_id):
    option = Books.objects.get(id = request.POST['select_book'])
    Authors.objects.get(id = author_id).books.add(option)
    return redirect(f'/authors/{author_id}')