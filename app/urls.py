from django.urls import path
from app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('tl/<str:text>/<str:to>/<str:from_>', views.translate, name='tl'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
