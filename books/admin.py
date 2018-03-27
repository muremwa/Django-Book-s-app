from django.contrib import admin
from .models import Book, Author

class BookInline(admin.TabularInline):
    model = Book
    extra = 3



class AuthorAdmin(admin.ModelAdmin):
    fields = ['author_id', 'name', 'picture', 'bio']

    inlines = [BookInline]




class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        ('book info', {'fields': ['book_id', 'title', 'number_of_pages', 'year_of_publication', 
        'author', 'publisher', 'genre']}),
        ('others', {'fields': ['book_cover', 'is_favourite']})
    ]

    list_display = ['book_id', 'title', 'votes']

    list_filter = ['year_of_publication']

    search_fields = ['title']


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)



