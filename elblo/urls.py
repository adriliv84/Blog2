from django.conf.urls import url, include
from django.contrib import admin
from posts import urls as postsURLs


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include(postsURLs))
]
