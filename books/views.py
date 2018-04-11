from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Book, Author
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView


# books homepage
class IndexView(generic.ListView):
    template_name = 'books/index.html'
    context_object_name = 'all_books'

    def get_queryset(self):
        return Book.objects.all()

# each book detail
def detail(request, book_id):
    the_book = get_object_or_404(Book, book_id=book_id)
    context = { 'the_book' : the_book }
    return render(request, 'books/book.html', context)

# books by same author
def same_author(request, the_name):
    author = Author.objects.get(name = the_name)
    books =  author.book_set.all()
    context = {
        'books' : books,
        'author': author
         }

    return render(request, 'books/same_author.html', context)


# author's details
def author_detail(request, the_name):
    author = get_object_or_404(Author, name=the_name)
    context = {'author':author}
    return render(request, 'books/author.html', context)


# voting for books
@login_required
def vote(request, the_book_id):
    book = get_object_or_404(Book, book_id=the_book_id)
    author_name = book.author
    author = Author.objects.get(name = author_name)
    books = author.book_set.all()

    try:
        to_vote = get_object_or_404(Book, book_id=request.POST['book'])

    except (KeyError, Book.DoesNotExist):
        # if you do not select anything
        return render(request, 'books/same_author.html', {
            'books': books,
            'author':author,
            'error_message': 'You did not select anything',
        })

    else:
        # add a vote to selected book
        to_vote.votes += 1
        to_vote.save()      
        # return a webpage
        return HttpResponseRedirect(reverse('books:index'))


# adding books
class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['book_id', 'title', 'author', 'publisher', 'number_of_pages', 'year_of_publication', 'genre', 'is_favourite', 'book_cover']