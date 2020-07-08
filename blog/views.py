from django.shortcuts import render
# Create your views here.

posts = [
    {
        'author': 'Alice',
        'title': 'Django',
        'content': 'Leraning from corey',
        'date_posted': '20200707'
    },
    {
        'author': 'Coco',
        'title': 'Javascript',
        'content': 'Leraning from corey',
        'date_posted': '20200707'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})