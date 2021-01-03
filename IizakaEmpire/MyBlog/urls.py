from django.urls import path,include
from rest_framework import routers
from . import views
from .views import Index, Blog, Categorys, TagAPI, AriticleAPI

app_name='MyBlog'

router = routers.DefaultRouter()
router.register('tag', TagAPI)
router.register('article', AriticleAPI)

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('blog/<slug:div>/<slug:slug>/', Blog.as_view(), name='blog'),
    path('search/<slug:kinds>/<int:search_type>/', Categorys.as_view(), name='search'),
    path('sitepolicy/', views.sitepolicy, name='policy'),
    path('_ah/warmup', views.warm_up, name='warmup'),
    path('markdownx/', include('markdownx.urls')),
]