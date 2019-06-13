from django.shortcuts import render

# Create your views here.

def page(request):
    return render(request, 'app/page.html')
