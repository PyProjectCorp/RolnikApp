from django.conf.urls import patterns, include, url
from django.contrib import admin
from home.views import HomepageView
from contact.views import MessageAddView
from animals.views import AnimalsView, AnimalsAddView
from allauth.account import urls as all_urls
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rolnikapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomepageView.as_view(), name='homepage'),
    url(r'^contact/', MessageAddView.as_view(), name='contact'),
    url(r'^animals/add/', login_required(AnimalsAddView.as_view()), name='animalsadd'),
    url(r'^animals/', login_required(AnimalsView.as_view()), name='animals'),
    url(r'^accounts/', include('allauth.urls')),
)
