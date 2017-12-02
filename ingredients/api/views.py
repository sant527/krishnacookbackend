from django.db.models import Q




from rest_framework.pagination import(
	LimitOffsetPagination,
	PageNumberPagination
	)

from rest_framework.filters import(
	SearchFilter,
	OrderingFilter,
	)

from rest_framework.generics import (
	CreateAPIView,
	DestroyAPIView,
	ListAPIView,
	UpdateAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView,
	RetrieveDestroyAPIView, #Blog API with Django Rest Framework 10 of 33 - Associate User with View Methods-8-hJeWQgYTQ 03:40 (use this to have preffilled and show the values in api view)
	)

from .serializers import (
	IngredientListSerializer,
	IngredientDetailSerializer,
	IngredientCreateUpdateSerializer,

	) 

#Blog API with Django Rest Framework 11 of 33 - Custom Permissions--0c88d24qzM (for permissions we have to import the following)

from rest_framework.permissions import(
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
	)

from .pagination import(
	IngredientLimitOffsetPagination,
	IngredientPageNumberPagination
	)

from .permissions import IsOwnerOrReadOnly
from ingredients.models import Ingredient

#knowledge1: order in alphabetical way


from django.db.models.functions import Lower
from rest_framework.filters import OrderingFilter

from ingredients.api.serializers import (TypeofIngredientSerializerforselectform,IngredientSerializer)

from rest_framework.response import Response

from typeofingredient.models import TypeOfIngredient

from ingredients.forms import IngredientForm10

from django_remote_forms.forms import RemoteForm



from django.core.serializers.json import DjangoJSONEncoder
import json
from django.http import HttpResponse
from django.middleware.csrf import CsrfViewMiddleware
from django.views.decorators.csrf import csrf_exempt

from django_remote_forms.forms import RemoteForm
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from ingredients.forms import IngredientForm10


@csrf_exempt
def my_ajax_view(request):
	csrf_middleware = CsrfViewMiddleware()

	response_data = {}
	if request.method == 'GET':
		# Get form definition
		form = IngredientForm10()
	elif request.method == 'POST':
		#request.POST = json.loads(request.body)
		# Process request for CSRF
		csrf_middleware.process_view(request, None, None, None)
		form_data = json.loads(request.body)
		form = IngredientForm10(form_data)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse("ingredients-api:singleform"))

	remote_form = RemoteForm(form)
	# Errors in response_data['non_field_errors'] and response_data['errors']
	response_data.update(remote_form.as_dict())

	response = HttpResponse(
		json.dumps(response_data, cls=DjangoJSONEncoder),
		content_type="application/json"
	)

	# Process response for CSRF
	csrf_middleware.process_response(request, response)
	return response






class CombineListViewforform(ListAPIView):
	
	def list(self, request, *args, **kwargs):
		return Response({
			"munit": Ingredient.MUNITS_CHOICES2,
			"typeofingredients": TypeofIngredientSerializerforselectform(TypeOfIngredient.objects.all(), many=True).data,
		})

class IngredientApi(ListAPIView):
	def list(self, request, *args, **kwargs):
		form = IngredientForm10()
		remote_form = RemoteForm(form)
		remote_form_dict = remote_form.as_dict()
		return Response(remote_form_dict)




class IngredientCreateAPIView(CreateAPIView): #Lecture 9 Create Serializer and Create View 
# Using IngredientCreateSerializer to IngredientCreateUpdateSerializer
	queryset = Ingredient.objects.all()
	serializer_class = IngredientCreateUpdateSerializer

	# Blog API with Django Rest Framework 10 of 33 - Associate User with View Methods-8-hJeWQgYTQ 02:22 (use perform_create to modify data )

	# def perform_create(self,serializer):
	#   #serializer.save(user=self.request.user, title='mytitle') this will change the title and the user Blog API with Django Rest Framework 10 of 33 - Associate User with View Methods-8-hJeWQgYTQ 02:45
	#   serializer.save(user=self.request.user)


class IngredientDetailAPIView(RetrieveAPIView):
	queryset = Ingredient.objects.all()
	serializer_class = IngredientDetailSerializer
	lookup_field = 'slug'    #knowledge1
	#lookup_url_kawrg = "abc" #knowledge1

class IngredientUpdateAPIView(RetrieveUpdateAPIView): #Blog API with Django Rest Framework 10 of 33 - Associate User with View Methods-8-hJeWQgYTQ 03:40 (use RetrieveUpdateAPIView to have preffilled and show the values in api view)
	queryset = Ingredient.objects.all()
	serializer_class = IngredientCreateUpdateSerializer
	lookup_field = 'slug' 
	# permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

	# def perform_update(self,serializer): # #Blog API with Django Rest Framework 10 of 33 - Associate User with View Methods-8-hJeWQgYTQ 03:55 (perform_create is used for creating and perform update is used for updating)
	#   serializer.save(user=self.request.user)

class IngredientDeleteAPIView(RetrieveDestroyAPIView):
	queryset = Ingredient.objects.all()
	serializer_class = IngredientDetailSerializer
	lookup_field = 'slug'

# class CaseInsensitiveOrderingFilter(OrderingFilter):
#   # ordering_fields = ('name')
#   # print(ordering_fields)

#   def filter_queryset(self, request, queryset, view):
#       ordering = self.get_ordering(request, queryset, view)

#       if ordering:
#           new_ordering = []
#           for field in ordering:
#               if field.startswith('-'):
#                   new_ordering.append(Lower(field[1:]).desc())
#               else:
#                   new_ordering.append(Lower(field).asc())
#           return queryset.order_by(*new_ordering)

#       return queryset

# class NormalOrderingFilter(OrderingFilter):
#   ordering_fields = ('name')


class CaseInsensitiveOrderingFilter(OrderingFilter):

	def filter_queryset(self, request, queryset, view):
		ordering = self.get_ordering(request, queryset, view)
		insensitive_ordering = getattr(view, 'ordering_case_insensitive_fields', ())

		if ordering:
			new_ordering = []
			for field in ordering:
				if field in insensitive_ordering:
					if field.startswith('-'):
						new_ordering.append(Lower(field[1:]).desc())
					else:
						new_ordering.append(Lower(field).asc())
					#new_ordering.append(Lower(field[1:]).desc() if field.startswith('-') else Lower(field).asc())
				else:
					new_ordering.append(field)
			return queryset.order_by(*new_ordering)

		return queryset



class IngredientListAPIView(ListAPIView):
	queryset = Ingredient.objects.all().order_by(Lower('name'))
	serializer_class = IngredientListSerializer
	filter_backends = [SearchFilter,CaseInsensitiveOrderingFilter]
	#search_fields = ['name','slug']
	#print(filter_backends)
	#ordering_fields = ('name')

	ordering_fields = ('__all__') # include both normal and case insensitive fields
	ordering_case_insensitive_fields = ('name') # put here only case insensitive fields
	#Builtint pagination
	#pagination_class = PageNumberPagination
	#pagination_class = LimitOffsetPagination
	#http://127.0.0.1:8000/api/ingredients/?limit=2&offset=2

	#pagination_class = IngredientLimitOffsetPagination
	pagination_class = IngredientPageNumberPagination

	# def eval_param(self, param):
 #        if param.startswith('-'):
 #            return param[1:]
 #        else:
 #            return param

 #    def get_queryset(self):
 #        queryset = self.queryset
 #        ordering = self.request.query_params.get('ordering', None)
 #        if ordering:
 #            queryset = queryset.order_by(
 #                *[Lower(self.eval_param(p)) for p in ordering.split(',')]
 #            )
 #        return queryset

 #    .extra(select={'lower_name':'lower(name)'}).order_by('lower_name')


	#searching the non builtin way

	# def filter_queryset(self, queryset):
	#   if "name" in self.request.query_params.get("ordering"):
	#       return CaseInsensitiveOrderingFilter().filter_queryset(self.request, queryset, self)
	#   else:
	#       queryset = OrderingFilter().filter_queryset(self.request, queryset, self)
	#       return SearchFilter().filter_queryset(self.request, queryset, self)


	def get_queryset(self, *args, **kargs):
		queryset_list = self.queryset
		query = self.request.GET.get("q")
		if query:
			queryset_list = queryset_list.filter(
				Q(name__icontains=query)|
				Q(slug__icontains=query)
				).distinct()
		return queryset_list
		
		# ordering = self.request.query_params.get('ordering', None)
  #       if ordering:
  #           queryset = queryset.order_by(
  #               *[Lower(self.eval_param(p)) for p in ordering.split(',')]
  #           )
  #         return queryset

		# return queryset_list

	#http://127.0.0.1:8000/api/ingredients/?search=hare&ordering=title using built in


#Blog API with Django Rest Framework 13 of 33 - Pagination with Rest Framework-p4B8zFVRmHI: 06:39 default setting of classes of the rest_framework can be set up in the settings file like permissions etc.

"""
	knowledge1 : Blog API with Django Rest Framework 6 of 33 - Retrieve API View aka Detail View-dWZB_F32BDg.mp4

	00:02:34 to  00:04:12

	lookup_field = 'slug'
	lookup_url_kawrg = "abc"


	then 

	url(r'^(?P<abc>[\w-]+)/$', IngredientDetailAPIView.as_view(), name='detail'), -- work

"""

"""
knowledge: Blog API with Django Rest Framework 11 of 33 - Custom Permissions--0c88d24qzM

permissions:  not authorization.

if user is logged in then 


"""