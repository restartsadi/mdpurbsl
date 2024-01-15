from django.shortcuts import render
from .models import NewsStream
# Create your views here.
def video(request):
    
    newsstream = NewsStream.objects.all()
    
    return render(request, 'index.html', {'newsstream': newsstream})

