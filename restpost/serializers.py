from rest_framework import serializers
from rest_framework.serializers import (
	ModelSerializer,
)
from restpost.models import Post
from restpost.models import Category




class listSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
			'id',
			'category',
			'title',
			'text',
		]

class addSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
			'category',
			'title',
			'text',
		]




class showSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
			'id',
			'category',
			'title',
			'text',
		]




class deleteSerializer(ModelSerializer):
	class Meta:
		model = Post



class updateSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
			'category',
			'title',
			'text',
		]