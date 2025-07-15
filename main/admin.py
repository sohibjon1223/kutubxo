from django.contrib import admin
from .models import Book  # <--- Book modelini import qilishni unutmaslik kerak

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # created_at bo'lishi uchun modelda mavjud bo‘lishi kerak
