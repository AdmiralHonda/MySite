from django.urls import path,include

from . import views
from .views import index,blog

app_name='MyBlog'

urlpatterns = [
    path('',index.as_view(),name='index'),
    path('blog/<slug:div>/<slug:blog_id>/',blog.as_view(),name='blog'),
    path('search/<slug:type>/<int:searchtype>/',views.Categorys,name='search'),
    path('sitepolicy/',views.sitepolicy,name='policy'),
    path('markdownx/',include('markdownx.urls')),
]