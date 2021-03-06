from django.template import loader
from django.http import HttpResponse

from .models import Post

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return HttpResponse(template.render(context, request))

def page_view(request):
    template = loader.get_template('page.html')
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return HttpResponse(template.render(context, request))
    