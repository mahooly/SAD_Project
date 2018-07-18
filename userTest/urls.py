"""userTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from userTest import settings
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^register_benefactor/', views.benefactor_registration, name='register'),
    url(r'^register_organization/', views.organization_registration, name='registerOrg'),
    url(r'^create_project/', views.project_creation, name='createProject'),
    url(r'^login/', views.mylogin, name='login'),
    url(r'^editprofileben/', views.update_benefactor_profile, name='editprofileben'),
    url(r'^editprofileorg/', views.update_organization_profile, name='editprofileorg'),
    url(r'^terms/', views.terms, name='terms'),
    url(r'^search_projects', views.list_projects, name='search_projects'),
    url(r'^logout', views.user_logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
