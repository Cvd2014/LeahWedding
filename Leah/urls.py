from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles import views as static_views
from settings import MEDIA_ROOT
from homepage import views as homeView

urlpatterns = [
    # Examples:
    # url(r'^$', 'Leah.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', static_views.serve),
    url(r'^$', homeView.get_index, name="home"),


]
