from django.conf.urls import url
from .views import PostListView, PostDetailView, contact


app_name = 'blog'

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='post_list'),
    url(r'^contact/$',contact , name='contact'),
    url(r'^(?P<slug>[\w-]+)/$', PostDetailView.as_view(), name='post_detail'),
]
