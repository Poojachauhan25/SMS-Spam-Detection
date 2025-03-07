from django.contrib import admin
from django.urls import path
from detection.views import home, check_spam

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Home page
    path('check-spam/', check_spam, name='check_spam'),  # Spam detection page
]
