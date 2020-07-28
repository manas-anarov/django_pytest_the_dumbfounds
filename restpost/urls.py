from restpost import views
from django.conf.urls import url

urlpatterns = [
	url(r'^pagination/list/$', views.PostPaginationListAPIView.as_view(), name='restpost-pagination-list'),
	url(r'^list/$', views.PostListAPIView.as_view(), name='restpost-list'),
	url(r'^add/$', views.AddPost.as_view(), name='restpost-add'),
	url(r'^(?P<id>[\w-]+)/$', views.ShowPost.as_view(), name='restpost-show'),
	url(r'^delete/(?P<id>[\w-]+)/$', views.DeletePost.as_view(), name='restpost-delete'),
	url(r'^edit/(?P<id>[\w-]+)/$', views.UpdatePost.as_view(), name='restpost-update'),
]