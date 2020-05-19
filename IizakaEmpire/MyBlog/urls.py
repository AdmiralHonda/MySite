from django.urls import path,include

from . import views
from .views import Index, Blog, Categorys

app_name='MyBlog'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('blog/<slug:div>/<slug:slug>/', Blog.as_view(), name='blog'),
    path('search/<slug:kinds>/<int:search_type>/', Categorys.as_view(), name='search'),
    path('sitepolicy/', views.sitepolicy, name='policy'),
    path('markdownx/', include('markdownx.urls')),
]