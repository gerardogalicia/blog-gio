from django.contrib import admin
from blog.models import ArticleCategory, Article

# Register your models here.


# Not necessary according to specs, but helps in organizing entries
class ArticleAdmin(admin.ModelAdmin):
    list_display =('title','category', 'created_on', 'last_updated')

admin.site.register(ArticleCategory)
admin.site.register(Article, ArticleAdmin)

