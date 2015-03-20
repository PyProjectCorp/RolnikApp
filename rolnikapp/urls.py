from django.conf.urls import patterns, include, url
from django.contrib import admin
from home.views import HomepageView
from contact.views import MessageAddView
from allauth.account import urls as all_urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rolnikapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomepageView.as_view(), name='homepage'),
    url(r'^contact/', MessageAddView.as_view(), name='contact'),
    url(r'^accounts/', include('allauth.urls')),
)
