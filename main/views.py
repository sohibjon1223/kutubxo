from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages  # ✅ Login xabarlari uchun
from django.core.paginator import Paginator  # ✅ Sahifalash uchun
from .models import Book, News
from .forms import BookForm, NewsForm

# 🏠 Bosh sahifa
def index(request):
    books = Book.objects.all()
    news = News.objects.all()
    return render(request, 'index.html', {'books': books, 'news': news})

# 🔐 Login
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'admin' and password == '1232':
            request.session['is_admin'] = True
            return redirect('admin_page')
        else:
            messages.error(request, 'Login yoki parol noto‘g‘ri!')

    return render(request, 'login.html')

# 🔓 Logout
def logout_view(request):
    request.session.flush()
    return redirect('login')

# 👨‍💻 Admin panel
def admin_page(request):
    if not request.session.get('is_admin'):
        return redirect('login')

    books = Book.objects.all()
    news = News.objects.all()

    # Formlarni POST'da saqlash
    if request.method == 'POST':
        if 'book-title' in request.POST:  # Kitob formi
            book_form = BookForm(request.POST, request.FILES, prefix='book')
            if book_form.is_valid():
                book_form.save()
        elif 'news-title' in request.POST:  # Yangilik formi
            news_form = NewsForm(request.POST, request.FILES, prefix='news')
            if news_form.is_valid():
                news_form.save()
        return redirect('admin_page')
    
    # Formlarni ko‘rsatish (GET)
    book_form = BookForm(prefix='book')
    news_form = NewsForm(prefix='news')

    return render(request, 'admin.html', {
        'book_form': book_form,
        'news_form': news_form,
        'books': books,
        'news_list': news,
    })

# 📝 Kitobni tahrirlash
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('admin_page')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form, 'book': book})

# 📰 Yangilikni tahrirlash
def edit_news(request, news_id):
    news = get_object_or_404(News, id=news_id)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            return redirect('admin_page')
    else:
        form = NewsForm(instance=news)
    return render(request, 'edit_news.html', {'form': form, 'news': news})

# 📚 Faqat kitoblar sahifasi — sahifalash bilan
def kitoblar_view(request):
    kitoblar_list = Book.objects.all().order_by('-id')  # yoki boshqa mavjud maydon
    paginator = Paginator(kitoblar_list, 6)
    page_number = request.GET.get('page')
    kitoblar = paginator.get_page(page_number)

    return render(request, 'kitoblar.html', {'kitoblar': kitoblar})


# 🗞 Faqat yangiliklar sahifasi
def yangiliklar_view(request):
    yangiliklar = News.objects.all().order_by('-created_at')
    paginator = Paginator(yangiliklar, 6)  # Har bir sahifada 6 ta yangilik
    page_number = request.GET.get('page')
    news_list = paginator.get_page(page_number)
    return render(request, 'yangiliklar.html', {'news_list': news_list})

# ℹ️ About sahifasi
def about(request):
    return render(request, 'about.html')

# ☎️ Aloqa sahifasi
def aloqa(request):
    return render(request, 'aloqa.html')
