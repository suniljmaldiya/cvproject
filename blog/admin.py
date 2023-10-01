from django.contrib import admin

# Register your models here.
from .models import Category, Post
# Register your models here.

admin.site.site_header = "Sunil Saini"
admin.site.site_title ="Sunil Saini"
admin.site.site_color="red"

# for configuration of Admin Panel

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','description','url','add_date')
    search_fields = ('title',)
    list_per_page = 50

admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','add_date',)
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 50
admin.site.register(Post,PostAdmin)

