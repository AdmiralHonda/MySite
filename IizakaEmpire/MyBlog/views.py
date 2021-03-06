from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse, Http404
from django.views.generic import TemplateView, ListView, DetailView
from .models import Article, Author, Category, Policy,Tag

class Index(ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'article'
    paginate_by = 5

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = Author.objects.all()
        context['categorys'] = Category.objects.all()
        return context


class Blog(DetailView):
    template_name = 'blog.html'
    model = Article
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = context['article'].tags.all()
        context['recommend'] = Article.objects.all()[:4]
        context['categorys'] = Category.objects.all()
        context['author'] = Author.objects.all()
        return context


class Categorys(ListView):
    
    template_name = 'index.html'
    paginate_by = 3
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = Author.objects.all()
        context['categorys'] = Category.objects.all()
        return context

    def get_queryset(self):
        if self.kwargs['search_type'] == 1 :
            self.search_category = get_object_or_404(Category, slug = self.kwargs['kinds'])
            return Article.objects.filter(category = self.search_category)
        elif self.kwargs['search_type'] == 2 :
            return Article.objects.filter(tags__slug = self.kwargs['kinds'])
        else:
            return Article.objects.all()

def sitepolicy(request):
    policy=get_object_or_404(Policy,id=1)

    contexts={
        'policy':policy,
    }

    return render(request,'static.html',contexts)

def warm_up(request):
    return HttpResponse("OK")