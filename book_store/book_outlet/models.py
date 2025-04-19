from django.core import validators
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street}, {self.postal_code}, {self.city}"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(
        Address, on_delete=models.CASCADE, null=True
    )  # 1 tác giả chỉ có 1 địa chỉ

    def full_name(self):        # tạo tên đầy đủ
        return f"{self.first_name} {self.last_name}"    

    def __str__(self):  # giúp hiển thị thông tin lên admin page rõ ràng
        return self.full_name()


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    # author là pointer trỏ đến author entry trong Author table
    # tạo quan hệ nhiều cuốn sách cùng 1 tác giả
    author = models.ForeignKey(
        Author,  # tạo quan hệ nhiều cuốn sách → một tác giả#
        on_delete=models.CASCADE,  # khi xóa tác giả, sách cũng bị xóa.
        null=True,
    )  # cho phép sách không có tác giả (tránh lỗi khi migrate).

    is_bestselling = models.BooleanField(default=False)
    # Harry Potter 1 => harry-potter-1
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.rating})"
