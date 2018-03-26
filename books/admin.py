from django.contrib import admin
from .models import Book, Author

class AuthorAdmin(admin.ModelAdmin):
    fields = ['author_id', 'name', 'picture', 'bio']



class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        ('book info', {'fields': ['book_id', 'title', 'number_of_pages', 'year_of_publication', 
        'author', 'publisher', 'genre']}),
        ('others', {'fields': ['book_cover']})
    ]


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)



