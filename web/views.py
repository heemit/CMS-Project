from django.shortcuts               import render, get_object_or_404
from django.http                    import JsonResponse
from django.views.decorators.csrf   import csrf_exempt
from django.core.files.storage      import default_storage
from django.core.files.base         import ContentFile
from django.conf                    import settings
from .models                        import Page

def page_view(request, url="home"):
    page = get_object_or_404(Page, url=url)
    return render(request, "base.html", {"page": page})

@csrf_exempt
def save_page(request):
    if request.method == "POST":
        url              =   request.POST.get("url")
        content          =   request.POST.get("content")
        show_header      =   request.POST.get("show_header") == "true"
        show_footer      =   request.POST.get("show_footer") == "true"

        page, _          =  Page.objects.get_or_create(url=url)
        page.content     =  content
        page.show_header =  show_header
        page.show_footer =  show_footer
        page.save()

        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "error"}, status=400)
