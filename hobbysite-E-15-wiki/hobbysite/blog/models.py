from django.db import models


class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    
    description = models.TextField()

    class Meta:
        ordering = ['name'] 

    def __str__(self):
        return self.name



class Article (models.Model):
    title = models.CharField(max_length=255) # Title of the thing, max 255 characters
    category = models.ForeignKey(ArticleCategory, null =True, on_delete=models.SET_NULL)
    entry = models.TextField()

    created_on = models.DateTimeField(auto_now_add = True)
    last_updated = models.DateTimeField(auto_now= True)

    class Meta:
        ordering = ['-created_on']  # Sorted by creation date in descending order

    def __str__(self):
        return self.title
    
    # super user info
    # User: 610
    # Password: gio