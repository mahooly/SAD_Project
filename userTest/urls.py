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
from django.contrib.auth.views import password_reset_complete, password_reset, password_reset_done, password_reset_confirm
from django.contrib import admin
from django.urls import path
from userTest import settings
from users import views


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^register/benefactor/', views.benefactor_registration, name='register'),
    url(r'^register/organization/', views.organization_registration, name='registerOrg'),
    url(r'^register/project/', views.project_creation, name='createProject'),
    url(r'^register/requirement/', views.submit_requirement, name='submit_requirement'),

    url(r'^login/', views.my_login, name='login'),
    url(r'^logout', views.user_logout, name='logout'),
    url(r'^password_reset_complete/', password_reset_complete, name='password_reset_complete'),
    url(r'^password_reset/', password_reset, name='password_reset'),
    url(r'^password_reset_done', password_reset_done, name='password_reset_done'),
    url(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', password_reset_confirm, name='password_reset_confirm'),

    url(r'^profile/edit_benefactor/', views.update_benefactor_profile, name='editprofileben'),
    url(r'^profile/edit_organization/', views.update_organization_profile, name='editprofileorg'),
    url(r'^edit_project/(?P<pId>[0-9A-Za-z_\-]+)', views.change_project, name='changeProject'),
    url(r'^profile/(?P<username>[a-zA-Z0-9]+)$', views.user_profile, name='profile'),
    url(r'^requests/pending/', views.waiting_requests, name='waiting_requests'),
    url(r'^requests/sent/', views.sent_requests, name='sent_requests'),
    url(r'^profile/delete/', views.delete_user, name='delete_user'),

    url(r'^admin/reports/', views.report_admin, name='report'),
    url(r'^admin/report_project/(?P<p_id>[a-zA-Z0-9]+)$', views.report_project, name='reportProject'),
    url(r'^admin/remove_report/(?P<r_id>[a-zA-Z0-9]+)$', views.remove_report, name='remove_report'),
    url(r'^admin/waiting_registers', views.waiting_registers, name='waiting_registers'),
    url(r'^admin/change_cities/', views.change_cities, name='changeCities'),
    url(r'^admin/change_categories/', views.change_categories, name='changeCategories'),
    url(r'^admin/change_abilities/', views.change_abilities, name='changeAbilities'),

    url(r'^search/projects/', views.list_projects, name='search_projects'),
    url(r'^search/requirements/', views.list_requirement, name='search_requirements'),
    url(r'^search/abilities', views.list_abilities, name='search_abilities'),

    url(r'^comment/(?P<username>[a-zA-Z0-9]+)$', views.rate_user, name='comment'),
    url(r'^project/(?P<username>[a-zA-Z0-9]+)/(?P<p_id>[a-zA-Z0-9]+)/$', views.project, name='project'),
    url(r'^send_request_org/(?P<username>[a-zA-Z0-9]+)/(?P<req_id>[a-zA-Z0-9]+)/', views.send_request_organization, name='send_request_org'),
    url(r'^send_request_benefactor/(?P<username>[a-zA-Z0-9]+)$', views.send_request_benefactor, name='send_request_ben'),
    url(r'^accept_request/', views.accept_request, name='accept_request'),
    url(r'^report_cash/', views.report_cash, name='reportCash'),

    url(r'^delete_requirement/', views.delete_requirement, name='delete_requirement'),
    url(r'^delete_project/', views.delete_project, name='delete_project'),
    url(r'^delete_request/', views.delete_request, name='delete_request'),
    url(r'^donate/', views.donate, name='donate'),

    url(r'^404/', views.handler404, name='404'),
    url(r'^500/', views.handler500, name='500'),
    url(r'^terms/', views.terms, name='terms'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


