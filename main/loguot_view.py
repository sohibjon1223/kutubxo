from django.contrib import messages  # xabarlar uchun

def logout_view(request):
    # Admin sessiyasini tozalash
    request.session.flush()
    
    # Xabar berish (ixtiyoriy)
    messages.success(request, "Muvaffaqiyatli chiqdingiz.")
    
    # Login sahifaga yo'naltirish
    return redirect('login')
