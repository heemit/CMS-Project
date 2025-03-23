from django.contrib             import admin
from django.urls                import path, include
from django.conf                import settings
from django.conf.urls.static    import static
from django.http                import HttpResponseRedirect

def redirect_admin(request):
    return HttpResponseRedirect('http://inland-gerri-heemit-0a6c5f26.koyeb.app/admin/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
