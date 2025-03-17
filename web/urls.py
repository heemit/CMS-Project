from django.urls                import path
from .                          import views
from django.conf                import settings
from django.conf.urls.static    import static

urlpatterns = [
    path("editor/", views.page_view, name="editor"),
    path("save/", views.save_page, name="save_page"),
    path("<path:url>/", views.page_view, name="page_view"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)