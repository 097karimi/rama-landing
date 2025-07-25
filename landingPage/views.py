from django.shortcuts import render
from .forms import ContactForm

def landing_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Optionally, send an email confirmation here
            return render(request, 'home.html', {'form': form, 'success_message': 'ایمیل شما دریافت شد ممنون از اعتماد شما به زودی جهت دانلود اپ راما به شما ایمیل ارسال خواهد شد'})
    else:
        form = ContactForm()

    return render(request, 'home.html', {'form': form})