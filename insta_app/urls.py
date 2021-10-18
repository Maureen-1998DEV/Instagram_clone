from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$', views.home, name='sign'),
    url('^home/$',views.index,name='index'),
    url('^new/image$', views.new_image, name='new-image'),
    url('^profile/$',views.profile,name='profile'),
    url('^search/', views.search_results, name='search_results'),
    url('^comment/(?P<image_id>\d+)', views.comment, name='comment'),
    url('^profiles/(\d+)',views.profiles,name='profiles'),
    url('^signup/$', views.signup, name='signup'),
    url('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)