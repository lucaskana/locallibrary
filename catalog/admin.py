from django.contrib import admin
from catalog.models import Author, Genre, Book, BookInstance, PriceRow, Product


# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)
# Register your models here.
#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(PriceRow)

class PriceRowInstanceInline(admin.TabularInline):
    model = PriceRow
    #exclude = ['price_value']

@admin.register(Product)
class ProductInstanceAdmin(admin.ModelAdmin):
    list_display = ('label','code','description')
    fieldsets = (
        (None, {
            'fields': ('label','code',)
        }),
        ('Details', {
            'fields': ('info','description')
        }),
    )
    inlines = [PriceRowInstanceInline]

#admin.site.register(BookInstance)