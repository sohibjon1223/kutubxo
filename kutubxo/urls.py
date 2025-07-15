# kutubxona/urls.py

from django.contrib import admin
from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),                     # Django admin paneli
    path('', views.index, name='index'),                 # Bosh sahifa
    path('admin-page/', views.admin_page, name='admin_page'),   # Maxsus admin sahifa (kitob va yangilik qo‘shish)

    # Tahrirlash sahifalari
    path('edit-book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('edit-news/<int:news_id>/', views.edit_news, name='edit_news'),

    # Asosiy menyu sahifalari
    path('kitoblar/', views.kitoblar_view, name='kitoblar'),
    path('yangiliklar/', views.yangiliklar_view, name='yangiliklar'),
    path('about/', views.about, name='about'),
    path('aloqa/', views.aloqa, name='aloqa'),

    # Kirish va chiqish
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

# Rasm/media fayllar uchun
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
