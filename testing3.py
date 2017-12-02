%load_ext autoreload
%autoreload 2

%autoreload

Reload all modules (except those excluded by %aimport) automatically now.
%autoreload 0

Disable automatic reloading.
%autoreload 1

Reload all modules imported with %aimport every time before executing the Python code typed.
%autoreload 2

Reload all modules (except those excluded by %aimport) every time before executing the Python code typed.


from ingredients.api.pagination import TypeofIngredientSerializer
typeofingredientserializer = TypeofIngredientSerializer()
print(repr(typeofingredientserializer))

from ingredients.api.pagination import TypeofIngredientSerializerother1
typeofingredientserializer = TypeofIngredientSerializerother1()
print(repr(typeofingredientserializer))