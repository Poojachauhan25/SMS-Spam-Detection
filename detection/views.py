from django.shortcuts import render
from .models import Message
from .spam_filter import is_spam

def home(request):
    """Home Page View"""
    return render(request, "index.html")

def check_spam(request):
    """Spam Detection Page View"""
    if request.method == "POST":
        text = request.POST.get("text")
        spam_status = is_spam(text)
        message = Message.objects.create(text=text, is_spam=spam_status)
        return render(request, "check_spam.html", {"message": message})
    return render(request, "check_spam.html")
