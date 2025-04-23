import os
import django

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "book_store.settings"  # 👈 Đổi nếu project tên khác
)
django.setup()

from book_outlet.models import Book, Author, Country, Address

# Xóa dữ liệu cũ
Book.objects.all().delete()
Author.objects.all().delete()
Country.objects.all().delete()
Address.objects.all().delete()

# Tạo quốc gia
vietnam = Country.objects.create(name="Vietnam", code="VN")
uk = Country.objects.create(name="United Kingdom", code="UK")
france = Country.objects.create(name="France", code="FR")

# Tạo địa chỉ
address1 = Address.objects.create(
    street="123 Lý Thường Kiệt", postal_code="70000", city="TP.HCM"
)
address2 = Address.objects.create(
    street="456 Yorkshire Rd", postal_code="Y01", city="London"
)
address3 = Address.objects.create(
    street="789 Hoàng Diệu", postal_code="30000", city="Hà Nội"
)

# Tạo tác giả kèm địa chỉ
author1 = Author.objects.create(
    first_name="Nguyễn", last_name="Thịnh", address=address1
)
author2 = Author.objects.create(
    first_name="Emily", last_name="Brontë", address=address2
)
author3 = Author.objects.create(
    first_name="Nguyễn", last_name="Thành Long", address=address3
)

# Tạo sách và gán tác giả
book1 = Book.objects.create(title="Con Mưa Ngang Qua", rating=10, author=author1)
book2 = Book.objects.create(title="Đồi Gió Hú", rating=9, author=author2)
book3 = Book.objects.create(title="Lặng Lẽ Sa Pa", rating=8, author=author3)

# Gán quốc gia phát hành (ManyToMany)
book1.published_countries.set([vietnam])
book2.published_countries.set([uk, france])
book3.published_countries.set([vietnam, france])

print("Books, Authors, Addresses, and Countries reset completed.")
