from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    re_path('^$',views.news_today,name='newsToday'),
    re_path(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews'),
    re_path(r'^search/', views.search_results, name='search_results'),
    re_path(r'^article/(\d+)',views.article,name ='article'),
    re_path(r'^new/article$', views.new_article, name='new-article')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# First we import the url function from the from the django.conf.urls . We then import the app's views module.
# We then create a ist named urlpatterns this will be a list of url instances for our app. We then create URL instances by calling the url function.
# We pass in the URL regular expression the view and a name keyword argument.