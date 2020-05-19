from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from MyBlog.models import Article

class MyBlogSitemap(Sitemap):
    changefreq="yearly"
    priority=1.0

    def items(self):
        return Article.objects.all()

    def lastmod(self,obj):
        return obj.pub_date

    def location(self,obj):
        return reverse('MyBlog:blog', args = [
            obj.category.slug,
            obj.slug,
        ])
    
class StaticSitemap(Sitemap):
    changefreq="weekly"
    priority=0.8

    def items(self):
        return ['MyBlog:index','MyBlog:policy']
    
    def location(self,items):
        return reverse(items)