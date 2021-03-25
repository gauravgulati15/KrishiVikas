"""mait URL Configuration

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
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path("summernote/", include("django_summernote.urls")),
    path("", include("home.urls", namespace="home")),
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("dashboard/", include("dashboard.urls", namespace="dashboard")),
    path("about-us/", include("aboutus.urls", namespace="aboutus")),
    path("blog/", include("blog.urls", namespace="blog")),
    path("contact/", include("contact.urls", namespace="contact")),
    path('products/', include('products.urls', namespace='products')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# X_FRAME_OPTIONS = 'SAMEORIGIN'

admin.site.site_header = "Krishi Vikas Admin Panel"
admin.site.site_title = "Krishi Vikas Admin"
admin.site.site_index_title = "Welcome To Krishi Vikas Admin Panel"