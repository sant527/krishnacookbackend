from rest_framework.serializers import (ModelSerializer, 
	HyperlinkedIdentityField,
	SerializerMethodField,
	ReadOnlyField,
	CharField
	)

from rest_framework.response import Response

from rest_framework import serializers

from typeofingredient.models import TypeOfIngredient


from ingredients.models import Ingredient


# from rest_framework import serializers

# class ChoicesField(serializers.Field):
#     def __init__(self, choices, **kwargs):
#         self._choices = choices
#         super(ChoicesField, self).__init__(**kwargs)

#     def to_representation(self, obj):
#         return self._choices[obj]

#     def to_internal_value(self, data):
#         return getattr(self._choices, data)


class TypeofIngredientSerializerforselectform(ModelSerializer):
	value = CharField(source='name')
	class Meta:
		model = TypeOfIngredient
		fields = ('name','value')


class IngredientSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    munit = serializers.SerializerMethodField()
    slug = serializers.SerializerMethodField()
    typeofingredient = serializers.SerializerMethodField()

    class Meta:
        model = Ingredient
        fields = ('name', 'munit', 'slug','typeofingredient')

    def get_name(self, obj):
        response = dict()
        response['value'] = obj.name
        response['type'] =  Ingredient._meta.get_field("name").get_internal_type()
        return response

    def get_munit(self, obj):
        response = dict()
        response['value'] = obj.munit
        response['type'] = Ingredient._meta.get_field("munit").get_internal_type()
        return response

    def get_slug(self, obj):
        response = dict()
        response['value'] = obj.slug
        response['type'] = Ingredient._meta.get_field("slug").get_internal_type()
        return response

    def get_typeofingredient(self, obj):
        response = dict()
        if obj.typeofingredient is not None: response['value'] = obj.typeofingredient.name
        if obj.typeofingredient is not None: response['type'] =  TypeOfIngredient._meta.get_field("name").get_internal_type()
        return response



class IngredientCreateUpdateSerializer(ModelSerializer):
	class Meta:
		model = Ingredient
		fields = [
			'name',
			'munit',
			'rate',
			'typeofingredient',
			'density_kg_per_lt',
			'density_pcs_per_kg',
			'density_pcs_per_lt',
		]


ingredient_detail_url = HyperlinkedIdentityField(
		view_name = 'ingredients-api:detail',
		lookup_field = 'slug'
		)

ingredient_detail_url_page = HyperlinkedIdentityField(
		view_name = 'ingredients:list'
		#lookup_field = 'slug'
		)



class IngredientListSerializer(ModelSerializer):
	# def get_absolute_url(self):
	#     return reverse("ingredients:detail", kwargs={"slug": self.slug})
	# similar to above one
	# typeofingredient = serializers.RelatedField(many=True)
	typeofingredient = ReadOnlyField(source='typeofingredient.name',default=None)
	url = HyperlinkedIdentityField(
		view_name = 'ingredients-api:detail',
		lookup_field = 'slug'
		) #we can put this outside so that it can be used by all
	# delete_url = HyperlinkedIdentityField(
	# 	view_name='ingredients-api:delete',
	# 	lookup_field = 'slug'
	# 	)
	#url_page = ingredient_detail_url_page
	# image = SerializerMethodField()
	# markdown = SerializerMethodField()
	# user = SerializerMethodField()

	
	# def get_typeofingredient(self, obj):
	# 	if obj.typeofingredient:
	# 		return obj.typeofingredient_name
	# 	return -1



	class Meta:
		model = Ingredient
		fields = '__all__'
		#depth = 1
		# fields = [
		# 	'url',
		# 	'id',
		# 	'name',
		# 	'slug',
		# 	'munit',
		# 	'pack_quantity',
		# 	'rate_per_pack',
		# 	'rate_per_munit',
		# 	'updated',
		# 	'timestamp',
		# 	#'user',   # knowledge 4 (even though logged in as abc we see the user id is default=1) Blog API with Django Rest Framework 10 of 33 - Associate User with View Methods-8-hJeWQgYTQ
		# 	#'delete_url', (dont want to expose this)
		# 	#'url_page',
		# ]

	# def get_user(self,obj):
	# 	return str(obj.user.username)

	# def get_markdown(self,obj):
	# 	obj.get_markdown()

	# def get_image(self,obj):
	# 	try:
	# 		image = obj.image.url
	# 	except:
	# 		image =  None
	# 	return image

class IngredientDetailSerializer(ModelSerializer):  #knowledge2
	#user = SerializerMethodField()
	url=ingredient_detail_url
	#image = SerializerMethodField()
	#markdown = SerializerMethodField()
	#url_page = ingredient_detail_url_page
	#when we declare something here we have to put it into the fileds here.
	class Meta:
		model = Ingredient
		fields = [
			'url',
			'id',
			'name',
			'slug',
			'munit',
			'pack_quantity',
			'rate_per_pack',
			'rate_per_munit',
			'updated',
			'timestamp',
			#w'url_page',
		]

	# def get_user(self,obj):
	# 	return str(obj.user.username)

	# def get_markdown(self,obj):
	# 	obj.get_markdown()

	# def get_image(self,obj):
	# 	try:
	# 		image = obj.image.url
	# 	except:
	# 		image =  None

	# 	return image