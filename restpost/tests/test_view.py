from django.db import connection
from django.urls import reverse
from rest_framework.test import APITestCase

from restpost.models import Post

class TestPostListAPpiView(APITestCase):
    def test_missing_species(self):

        self.species_rabbit = Post.objects.create()

        with connection.cursor() as cursor:
            cursor.execute('DELETE FROM category title WHERE id =%s', [self.post.id])