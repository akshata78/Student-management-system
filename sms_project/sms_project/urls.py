from django.contrib import admin
from django.urls import path
from smsapp.views import home, create, remove
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home,name="home"),
    path("create", create, name = "create"),
    path("remove/<int:id>", remove, name = "remove")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


