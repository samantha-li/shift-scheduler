from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')), # new
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^db', hello.views.db, name='db'),
    url(r'^select', hello.views.select, name='select'),
    url(r'^shift-selection', hello.views.select_shifts, name='shift-selection'),
    url(r'^set-shifts', hello.views.set_shifts, name='set-shifts'),
    # url(r"^account/", include("account.urls")),
]
