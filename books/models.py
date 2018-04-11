from django.db import models    
from django.urls import reverse


# table for authors
class Author(models.Model):
    author_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    bio = models.TextField()
    picture = models.FileField(upload_to='authors', default='authors/defaulta.png')

    def __str__(self):
        return self.name


# table for books
class Book(models.Model):
    book_id = models.CharField(max_length=200, primary_key=True)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    publisher = models.CharField(max_length=400)
    number_of_pages = models.IntegerField()
    year_of_publication = models.DateField()
    genre = models.CharField(max_length=200)
    is_favourite = models.BooleanField()
    date_added = models.DateTimeField(auto_now_add=True)
    book_cover = models.FileField(upload_to='books_cover', default='books_cover/default.png')
    votes = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('books:detail', kwargs={'book_id': self.book_id})

    def __str__(self):
        return '{} by {}'.format(self.title, self.author)

    def full_detail(self):
        details = '{} is a {}-page {} book written by {} and published by {} date {}'.format(self.title, self.number_of_pages, self.genre, self.author, self.publisher, self.year_of_publication)
        return details


