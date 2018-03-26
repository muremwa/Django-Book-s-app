from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Book, Author
from django.urls import reverse


# books homepage
def index(request):
    all_books = Book.objects.all()
    context = {'all_books': all_books,}
    return render(request, 'books/index.html', context)


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
