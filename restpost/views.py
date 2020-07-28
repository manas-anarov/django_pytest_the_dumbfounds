from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from django.http import JsonResponse

from .serializers import (
	listSerializer,
	addSerializer,
	showSerializer,
	deleteSerializer,
	updateSerializer
	)

from rest_framework.generics import (CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView)
from rest_framework.response import Response

from restpost.models import Post
from restpost.models import Category


from rest_framework.permissions import (
	IsAuthenticated,
	AllowAny,
	)


from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import SessionAuthentication

from rest_framework.filters import (
		SearchFilter,
		OrderingFilter,
	)

from .pagination import PostLimitOffsetPagination, PostPageNumberPagination

class PostListAPIView(ListAPIView):
	serializer_class = listSerializer
	queryset = Post.objects.all()

class AddPost(CreateAPIView):
	authentication_classes = (TokenAuthentication, SessionAuthentication)
	permission_classes = (IsAuthenticated,)
	serializer_class = addSerializer
	queryset = Post.objects.all()

	def perform_create(self, serializer):
		serializer.save(author = self.request.user.id)


class ShowPost(RetrieveAPIView):
	queryset = Post.objects.all()
	serializer_class = showSerializer
	lookup_field = 'id'


class DeletePost(DestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = deleteSerializer
	lookup_field = 'id'


class UpdatePost(RetrieveUpdateAPIView):
	queryset = Post.objects.all()
	serializer_class = updateSerializer
	lookup_field = 'id'


class PostPaginationListAPIView(ListAPIView):
	serializer_class = listSerializer
	permission_classes = [AllowAny]
	filter_backends= [SearchFilter, OrderingFilter]
	search_fields = ['user__first_name','user__last_name']
	pagination_class = PostPageNumberPagination
	queryset = Post.objects.all()

	# def get_queryset(self, *args, **kwargs):
	# 	queryset_list = Post.objects.all().order_by('id')
	# 	query = self.request.GET.get("category")
	# 	if query:
	# 		if query != "0":
	# 			queryset_list = queryset_list.filter(
	# 					Q(category__id_cat__icontains=query)
	# 					).distinct()
		
	# 	if queryset_list.exists():
	# 		return queryset_list
	# 		# raise NotFound()
	# 	else:
	# 		raise NotFound()
	# 	# return queryset_list
