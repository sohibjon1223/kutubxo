

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='books/')
    created_at = models.DateTimeField(auto_now_add=True)  # ⬅️ Sana qo‘shildi

    def __str__(self):
        return self.title


from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='news_images/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # 🆕 Qo‘shildi

    def __str__(self):
        return self.title
