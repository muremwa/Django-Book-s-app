from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    # books/
    path('', views.index, name='index'),

    # books/3
    path('<int:book_id>/', views.detail, name='detail'),

    # books/booksbydrew
    path('booksby<the_name>/', views.same_author, name='same-author'),

    # books/drew
    path('author<the_name>/', views.author_detail, name='author'),

]