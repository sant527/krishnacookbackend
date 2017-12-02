from rest_framework.pagination import(
	LimitOffsetPagination,
	PageNumberPagination
	)

from rest_framework.renderers import JSONRenderer

from rest_framework.serializers import (ModelSerializer, 
	HyperlinkedIdentityField,
	SerializerMethodField,
	CharField,
	ReadOnlyField
	)

from typeofingredient.models import TypeOfIngredient


from rest_framework.response import Response

from ingredients.models import Ingredient

from ingredients.api.serializers import TypeofIngredientSerializerforselectform

# from .custom_drf_searilizer import YourPagination (not used)

class IngredientLimitOffsetPagination(LimitOffsetPagination):
	default_limit = 2
	max_limit = 3



class IngredientPageNumberPagination(PageNumberPagination):
	page_size = 10000
	page_size_query_param = "size"

	def get_paginated_response(self, data):
		return Response({
			'links': {
			   'next': self.get_next_link(),
			   'previous': self.get_previous_link()
			},
			'count': self.page.paginator.count,
			'total_pages': self.page.paginator.num_pages,
			'page_size': self.page_size,
			'page_number': self.page.number,
			'typeofingredients': TypeofIngredientSerializerforselectform(TypeOfIngredient.objects.all(), many=True).data,
			'munit': Ingredient.MUNITS_CHOICES2,
			'results': data,
		})

#this it most useful for pagination:

#max_limit how it is used.
#http://127.0.0.1:8000/api/ingredients/?limit=100&offset=2%22
#"next": "http://127.0.0.1:8000/api/ingredients/?limit=3&offset=3",


#default:
#http://127.0.0.1:8000/api/ingredients/
#"next": "http://127.0.0.1:8000/api/ingredients/?limit=2&offset=2",


