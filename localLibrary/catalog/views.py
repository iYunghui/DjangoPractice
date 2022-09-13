from django.shortcuts import render
from django.views import generic
from .models import Genre, Language, Book, BookInstance, Author

# Create your views here.
def index(request):

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1;

    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.all().count()
    num_language_type = Language.objects.all().count()
    num_genre = Genre.objects.all().count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_language_type': num_language_type, 
        'num_genre': num_genre,
        'num_visits': num_visits
    }

    return render(request, 'index.html', context=context)


def author(request):
    render()


class BookListView(generic.ListView):
    model = Book
    paginate_by = 1

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author


class AuthorDetailView(generic.DetailView):
    model = Author