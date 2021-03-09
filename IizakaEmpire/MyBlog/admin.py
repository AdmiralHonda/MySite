from django.contrib import admin
from .models import Article, Kinds, Category, Tag, Author, Policy
from markdownx.admin import MarkdownxModelAdmin
# Register your models here.
admin.site.register(Article,MarkdownxModelAdmin)
admin.site.register(Category)
admin.site.register(Kinds)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Policy)