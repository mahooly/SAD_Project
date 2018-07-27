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
    url(r'^profile/(?P<username>[a-zA-Z0-9]+)$', views.user_profile, name='profile'),
    url(r'^comment/(?P<username>[a-zA-Z0-9]+)$', views.rate_user, name='comment'),
    url(r'^project/(?P<username>[a-zA-Z0-9]+)/(?P<pId>[a-zA-Z0-9]+)/$', views.project, name='project'),
    url(r'^submit_requirement/', views.submit_requirement, name='submit_requirement'),
    url(r'^search_requirements/', views.list_requirement, name='search_requirements'),
    url(r'^waiting_registers', views.waiting_registers, name='waiting_registers'),
    url('^send_request_org/(?P<username>[a-zA-Z0-9]+)/(?P<reqId>[a-zA-Z0-9]+)/', views.send_request_organization, name='send_request_org'),
    url('^reports/', views.report_admin, name='report'),
    url('^search_abilities',views.list_abilities,name='search_abilities')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

