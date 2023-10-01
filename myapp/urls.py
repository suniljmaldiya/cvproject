
from django.urls import path, include
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import blogpost,category

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name=""),
    path('resume/',views.resume,name="resume"),
    path('portfolio/',views.portfolio,name="portfolio"),
    path('blog/',views.blog,name="blog"),
    path('contact/',views.contact,name="contact"),
    path('postcreation/',views.postcreation,name="postcreation"),
    path('blogpost/<slug:url>',blogpost),
    path('category/<slug:url>',views.category),
    path('tinymce/', include('tinymce.urls')),








]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

