import os
import django

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "book_store.settings"
)  # 👈 Đổi thành tên project thật
django.setup()

from book_outlet.models import Book, Author

# Xóa dữ liệu cũ
Book.objects.all().delete()
Author.objects.all().delete()

# Tạo tác giả mẫu
author1 = Author.objects.create(first_name="Nguyễn", last_name="Thịnh")
author2 = Author.objects.create(first_name="Emily", last_name="Brontë")
author3 = Author.objects.create(first_name="Nguyễn", last_name="Thành Long")

# Tạo sách có liên kết đến tác giả
Book.objects.create(title="Con Mưa Ngang Qua", rating=10, author=author1)
Book.objects.create(title="Đồi Gió Hú", rating=9, author=author2)
Book.objects.create(title="Lặng Lẽ Sa Pa", rating=8, author=author3)

print("Books and Authors reset completed.")
