from django.conf.urls import include, url
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'djangoapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # 首页
    url(r'^$', views.getIndex, name='getIndex'),

    # logout
    url(r'^logout/$', views.logout, name='logout'),
]
