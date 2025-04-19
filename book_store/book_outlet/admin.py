from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    
    list_filter = ('author', 'rating')  # lọc theo tác giả và điểm đánh giá
    list_display = ('title', 'author')  # hiển thị cột tiêu đề và tác giả


admin.site.register(Book, BookAdmin)
