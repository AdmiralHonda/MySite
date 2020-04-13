from django.shortcuts import render,get_list_or_404,get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse,Http404
from .models import Article,Author,Category
# Create your views here.

def index(request):

    try:
        article=Article.objects.all()

        author=Author.objects.all()

        pagenate=Paginator(article,5)

        if request.GET:
            p=request.GET.get('page')
            p=int(p)
        else:
            p=1

        putart=pagenate.get_page(p)
        page_num=pagenate.page_range
    
        contents={
            'author':author,
            'article':article,
            'page_num':page_num,
            'current_page':p,
        }

        return render(request,'index.html',contents)
    except (KeyError,Article.DoesNotExist):
        return Http404("お探しのコンテンツが見つかりませんでした。\n")
    else:
        return HttpResponse("障害が発生中です。\nお時間を置いてのアクセスをお願い致します。")

def blog(request,div,blog_id):
    
    putart=get_object_or_404(Article,slug=blog_id)
    recommend=Article.objects.all()[:4]

    tags_list=putart.tags.all()

    contents={
        'article':putart,
        'recommend':recommend,
        'tags':tags_list,
        'category':putart.category,
    }

    return render(request,'blog.html',contents)

def Categorys(request,type,searchtype):

    try:
        if searchtype==1:
            article=Article.objects.select_related('category').filter(category__slug=type)
        elif searchtype==2:
            article=Article.objects.select_related('tags').filter(tags__slug=type)
        else:
            return Http404
    
        article_List=[]

        author=Author.objects.all()

        pagenate=Paginator(article,5)

        if request.GET:
            p=request.GET.get('page')
            p=int(p)
        else:
            p=1

        putart=pagenate.get_page(p)
        page_num=pagenate.page_range
    
        contents={
            'author':author,
            'article':putart,
            'page_num':page_num,
            'current_page':p,
        }

        return render(request,'index.html',contents)
    except (KeyError,Article.DoesNotExist,Category.DoesNotExist):
        return Http404("お探しのコンテンツが見つかりませんでした。\n")
    else:
        return HttpResponse("障害が発生中です。\nお時間を置いてのアクセスをお願い致します。")
