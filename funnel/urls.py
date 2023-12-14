from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView


urlpatterns = [
    path('',  include("app.urls")),
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='admin/', permanent=True)),
    *static(settings.STATIC_URL, document_root=settings.BASE_DIR), # pathes for static files
] 
