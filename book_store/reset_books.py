# reset_books.py
import os
import django

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "your_project.settings"
)  # đổi thành tên project của bạn
django.setup()

from book_outlet.models import Book

Book.objects.all().delete()

Book.objects.create(title="Con Mưa Ngang Qua", rating=10)
Book.objects.create(title="Đồi Gió Hú", rating=9)
Book.objects.create(title="Lặng Lẽ Sa Pa", rating=8)

print("Books reset completed.")
