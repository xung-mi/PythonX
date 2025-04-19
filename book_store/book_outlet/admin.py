from django.contrib import admin
from .models import Book, Author, Address


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

    list_filter = ("author", "rating")  # lọc theo tác giả và điểm đánh giá
    list_display = ("title", "author")  # hiển thị cột tiêu đề và tác giả


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")  # hiển thị tên trong admin


class AddressAdmin(admin.ModelAdmin):
    list_display = ("street", "postal_code", "city")  # hiển thị tên trong admin


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address, AddressAdmin)
# admin.site.register(Author)
