from django.conf.urls import url
from . import views
from django.urls import path
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


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)