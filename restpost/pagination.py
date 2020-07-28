from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
    )

from rest_framework.response import Response

class PostLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 10


class PostPageNumberPagination(PageNumberPagination):
	page_size_query_param = 'limit'
	def get_paginated_response(self, data):
		response = super(PostPageNumberPagination, self).get_paginated_response(data)
		response.data['total_pages'] = self.page.paginator.num_pages
		response.data['has_more'] = True
		return response
