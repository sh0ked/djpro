from django.contrib import admin
from nuash.models import Article


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title', 'full_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = ('title', 'full_text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['title']

admin.site.register(Article, ArticleAdmin)