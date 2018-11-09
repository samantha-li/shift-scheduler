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
    path('accounts/', include('accounts.urls')), # new
    path('accounts/login', 'django.contrib.auth.views.login'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^select', hello.views.select, name='select'),
    url(r'^shift-selection', hello.views.select_shifts, name='shift-selection'),
    url(r'^set-shifts', hello.views.set_shifts, name='set-shifts'),
    path('admin/', admin.site.urls),
    url(r"^account/", include("account.urls")),
]
