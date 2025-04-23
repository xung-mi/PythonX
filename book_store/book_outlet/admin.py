from django.contrib import admin
from .models import Book, Author, Address, Country, Post, Tag

"""
    ManyToManyField → không được dùng trực tiếp trong list_display
    Phải viết hàm xử lý thủ công, trả về chuỗi hoặc dạng hiển thị phù hợp.
"""


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

    list_filter = ("author", "rating")  # lọc theo tác giả và điểm đánh giá
    list_display = ("title", "author")  # hiển thị cột tiêu đề và tác giả


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "address",
        "email_address",
    )  # hiển thị tên trong admin


class AddressAdmin(admin.ModelAdmin):
    list_display = ("street", "postal_code", "city")  # hiển thị tên trong admin


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "excerpt", "date", "slug", "content", "author", "get_tags")

    def get_tags(self, obj):
        return ", ".join(tag.caption for tag in obj.tags.all())

    get_tags.short_description = "Tags"


class TagAdmin(admin.ModelAdmin):
    list_display = ("caption",)


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Country)

# admin.site.register(Author)
