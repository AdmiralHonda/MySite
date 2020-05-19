from django.shortcuts import render,get_list_or_404,get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse,Http404
from django.views.generic import TemplateView,ListView,DetailView
from .models import Article,Author,Category,Policy
# Create your views here.

class index(ListView):
    model=Article
    template_name='index.html'
    context_object_name='article'
    paginate_by = 3

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['author']=Author.objects.all()

        return context


class blog(DetailView):
    template_name='blog.html'
    model=Article

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['tags']=context['article'].tags.all()
        context['recommend']=Article.objects.all()[:4]
        return context


def Categorys(request,type,searchtype):

    try:
        if searchtype==1:
            article=Article.objects.select_related('category').filter(category__slug=type)
        elif searchtype==2:
            article=Article.objects.filter(tags__slug=type)
        else:
            return Http404

        author=Author.objects.all()

        pagenate=Paginator(article,5)

        if request.GET:
            p=request.GET.get('page')
            p=int(p)
        else:
            p=1

        putart=pagenate.get_page(p)
        page_num=pagenate.page_range
        categ=Category.objects.all()
        contents={
            'author':author,
            'article':putart,
            'page_num':page_num,
            'current_page':p,
            'category':categ,
        }

        return render(request,'index.html',contents)

    except (KeyError,Article.DoesNotExist,Category.DoesNotExist):
        return Http404("お探しのコンテンツが見つかりませんでした。\n")
    else:
        return HttpResponse("障害が発生中です。\nお時間を置いてのアクセスをお願い致します。")

def sitepolicy(request):
    policy=get_object_or_404(Policy,id=1)

    contexts={
        'policy':policy,
    }

    return render(request,'static.html',contexts)