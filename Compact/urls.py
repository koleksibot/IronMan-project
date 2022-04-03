"""Compact URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.contrib.staticfiles.urls import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Compact API",
      default_version='v0.0.1',
      description="Test description",
      terms_of_service="http://compact.in/policies/terms/",
      contact=openapi.Contact(email="contact@compact.local"),
      license=openapi.License(name="Test License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

admin.site.site_header = "AtaOta Admin"
admin.site.site_title = "AtaOta"

urlpatterns = [
    # path("", TemplateView.as_view(template_name="index.html"), name="app"),
    path('Account/', include('Account.urls')),
    path('aboutUs/', include('AboutUs.urls')),
    path('AllProfile/', include('AllProfile.urls')),
    path('Products/', include('products.urls')),

    path('API/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # For Development
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # For Development


    path('CompactAdmin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
   re_path("", TemplateView.as_view(template_name="index.html"), name="app")
]
