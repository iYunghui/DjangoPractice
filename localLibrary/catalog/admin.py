from django.contrib import admin
from .models import Genre, Language, Book, BookInstance, Author

class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'uniqueId')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {'fields': ('book', 'imprint', 'uniqueId')}),
        ('Availability', {'fields': ('status', 'due_back')}),
    )

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

class BookInline(admin.TabularInline):
    model = Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]

# Register your models here.
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Author, AuthorAdmin)
