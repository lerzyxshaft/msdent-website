from django.shortcuts import render

def index(request):
    context = {
        'title': 'Strona główna',
        'active_page': 'home'
    }
    return render(request, 'index.html', context)

