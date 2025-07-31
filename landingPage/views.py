# views.py
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Visitor
import datetime

def landing_page(request):
    if not request.session.get('has_visited'):
        # Mark the session as visited
        request.session['has_visited'] = True
        
        # Save visitor information in the database
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        referer = request.META.get('HTTP_REFERER', '')
        
        visitor = Visitor(
            ip_address=request.META.get('REMOTE_ADDR'),
            user_agent=user_agent,
            referer=referer
        )
        visitor.save()

    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request, 'home.html', {
                'form': form,
                'success_message': 'ایمیل شما دریافت شد ممنون از اعتماد شما به زودی جهت دانلود اپ راما به شما ایمیل ارسال خواهد شد'
            })

    return render(request, 'home.html', {'form': form})