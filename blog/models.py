from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField
# Create your models here.


#for category

class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categorymedia/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.title

    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:120px; height:60px;"/>'.format(self.image))

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=500)
    content = HTMLField()
    url = models. CharField(max_length=100)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='postmedia/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.title
    

