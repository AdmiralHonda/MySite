from django.urls import path,include

from . import views

app_name='MyBlog'

urlpatterns = [
    path('',views.index,name='index'),
    path('blog/<slug:div>/<slug:blog_id>/',views.blog,name='blog'),
    path('search/<slug:type>/<int:searchtype>/',views.Categorys,name='search'),
    path('sitepolicy/',views.sitepolicy,name='policy'),
    path('markdownx/',include('markdownx.urls')),
]