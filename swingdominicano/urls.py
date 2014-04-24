from django.conf.urls import patterns, include, url
import settings 
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'swingdominicano.views.home', name='home'),
    url(r'^$', 'app.views.index', name='index'),
    url(r'^post$', 'post.views.index', name='post'),
    url(r'^photos$', 'photos.views.list_photos', name='photos'),
    url(r'^contact$', 'contact.views.contact', name='contact'),
    url(r'^video$', 'video.views.video', name='video'),
    (r'^tinymce/', include('tinymce.urls')),
    # url(r'^swingdominicano/', include('swingdominicano.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #patterns('',
        #static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
       #(r'^/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    #)