from django.shortcuts import render, HttpResponse
from . import  models

def hello(request):
    return HttpResponse('<h1>Hello World!</h1>')

#для отображения в html файле
def blog_view(request):
    blog = models.Blog.objects.all()
    return render(request, 'blog.html',  {'blog':blog})