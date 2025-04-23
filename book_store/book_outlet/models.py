from django.core import validators
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

"""
    Khi nào dùng quan hệ nào? 1 1, 1 nhiều (foreign key), nhiều nhiều
        -   Foreign key: 
                A → nhiều B
                Dùng khi bạn muốn thiết lập quan hệ Một-nhiều
                Bên Many chứa ForeignKey trỏ về bên One 
                    Vì mỗi B phải biết nó thuộc về A nào, nên nó cần lưu ID của A.
                Ví dụ: Một tác giả có thể viết nhiều bài viết => Post có ForeignKey trỏ đến Author
        -   OneToOneField:
                Dùng khi bạn muốn thiết lập quan hệ Một-một
                Một bản ghi trong bảng A chỉ liên kết duy nhất một bản ghi trong bảng B và ngược lại.
                Đặt OneToOneField ở bên nào?
                    Khóa liên kết đặt bên nào cũng được. Nhưng nên đặt ở "bên phụ thuộc"
                Ví dụ: 
                    Address và Author
                    Nếu đặt khóa liên kết ở Address => Address cần biết nó thuộc về Author nào
                    Nếu đặt khóa liên kết ở Author  => Author cần biết nó liên kết tới địa chỉ nào, ko có cũng ko sao
                    Vì địa chỉ không có ý nghĩa nếu không có tác giả
                    => Address là bên phụ thuộc => nên là nơi chứa khóa liên kết.
        -   ManyToManyField:
                A ↔ nhiều B, và B ↔ nhiều A.
                Dùng khi bạn có nhiều bản ghi ở bảng A liên kết với nhiều bản ghi ở bảng B
                Đặt khóa liên kết Tùy ý, đặt ở bên nào cũng được, vì Django sẽ tạo bảng trung gian.
        
    Các khái niệm:
    Bên phụ thuộc là bên không nên tồn tại nếu bên còn lại bị xoá
"""


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)

    class Meta:
        verbose_name = "Country"  # Tên hiển thị số ít trong admin
        verbose_name_plural = "Countries"  # Tên hiển thị số nhiều
        ordering = ["name"]  # Mặc định sắp xếp theo tên
        db_table = "country"  # Tên bảng trong cơ sở dữ liệu
        unique_together = [["name", "code"]]  # Tên và mã quốc gia không được trùng

    def __str__(self):
        return self.name


class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Address"  # Tên hiển thị số ít
        verbose_name_plural = (
            "Addresses"  # Tên hiển thị số nhiều (không phải "Addresss")
        )
        ordering = [
            "city",
            "street",
        ]  # Sắp xếp mặc định: theo thành phố, sau đó theo đường
        db_table = "address"  # Tên bảng cụ thể
        unique_together = [
            ["street", "postal_code", "city"]
        ]  # Không được trùng hoàn toàn địa chỉ

    def __str__(self):
        return f"{self.street}, {self.postal_code}, {self.city}"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(
        Address, on_delete=models.CASCADE, null=True
    )  # 1 tác giả chỉ có 1 địa chỉ
    email_address = models.EmailField(("Email address"), max_length=254, null=True)

    def full_name(self):  # tạo tên đầy đủ
        return f"{self.first_name} {self.last_name}"

    def __str__(self):  # giúp hiển thị thông tin lên admin page rõ ràng
        return self.full_name()

    class Meta:
        verbose_name_plural = "Authors"


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

    """
        Django sẽ tự tạo bảng trung gian (mapping table) để lưu các mối quan hệ.
        Xóa một country chỉ xóa kết nối, không xóa sách liên quan.
        Ví dụ:
            1 book xuất bản ở 2 country → bảng trung gian có 2 dòng.
    """
    published_countries = models.ManyToManyField(Country, null=False)

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


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)  # Đoạn trích ngắn của bài viết
    image_name = models.CharField(max_length=100)  #  Tên file ảnh
    date = models.DateField(auto_now=True)
    slug = models.SlugField(
        unique=True
    )  # Chuỗi định danh SEO cho URL. Index mặc định, unique tạo index luôn
    content = models.TextField(validators=[MinValueValidator(10)])
    author = models.ForeignKey(
        Country, on_delete=models.SET_NULL, null=True, related_name="posts"
    )
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.title} ({self.date})"

    class Meta:
        verbose_name_plural = "Posts"
