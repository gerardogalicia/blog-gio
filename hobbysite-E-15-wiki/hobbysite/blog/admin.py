from django.contrib import admin
from blog.models import ArticleCategory, Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display =('title','category', 'created_on', 'last_updated')

admin.site.register(ArticleCategory)
admin.site.register(Article, ArticleAdmin)



# Register your models here.
