from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('sucesso/', views.obrigado, name='obrigado'),
    # path('redirect-cad/', views.redirect_cadastro, name='redirect-cad'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)