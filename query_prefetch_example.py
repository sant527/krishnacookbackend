queryset_list = (Recipe
				.objects
				.select_related('mass_unit','volume_unit','pieces_unit')
				.all()
				.extra(
					select={'lower_name':'lower(recipes_recipe.name)'}
					)
				.order_by('lower_name')
				.prefetch_related(
					Prefetch(
						'recipe_positions', 
						queryset=RecipePosition
							.objects
							.select_related(
								'ingredient',
								'mass_unit',
								'volume_unit',
								'pieces_unit'
								)
							.extra(
								select={'lower_name1':'lower(recipes_recipeposition.name)'}
								)
							.order_by('lower_name1'),
						to_attr = 'recipe_ingredient_list_name'
						),
					Prefetch(
						'recipe_positions', 
						queryset=RecipePosition
							.objects
							.select_related(
								'ingredient',
								'mass_unit',
								'volume_unit',
								'pieces_unit'
								)
							.extra(
								select={'lower_name1':'lower(recipes_recipeposition.name)'}
								)
							.order_by('-lower_name1'),
						to_attr = 'recipe_ingredient_list_name_reverse'
						),
					Prefetch(
						'recipe_positions', 
						queryset=RecipePosition
							.objects
							.select_related(
								'ingredient',
								'mass_unit',
								'volume_unit',
								'pieces_unit'
								)
							.order_by('sequence_number'),
						to_attr = 'recipe_ingredient_sequence'
						),
					Prefetch(
						'recipe_positions', 
						queryset=RecipePosition
							.objects
							.select_related(
								'ingredient',
								'mass_unit',
								'volume_unit',
								'pieces_unit'
								)
							.order_by('-sequence_number'),
						to_attr = 'recipe_ingredient_sequence_reverse'
						),
					Prefetch(
						'recipe_positions', 
						queryset=RecipePosition
							.objects
							.select_related(
								'ingredient',
								'mass_unit',
								'volume_unit',
								'pieces_unit'
								)
							.order_by('updated'),
						to_attr = 'recipe_ingredient_updated'
						),
					Prefetch(
						'recipe_positions', 
						queryset=RecipePosition
							.objects
							.select_related(
								'ingredient',
								'mass_unit',
								'volume_unit',
								'pieces_unit'
								)
							.order_by('updated'),
						to_attr = 'recipe_ingredient_updated_reverse'
						),
						Prefetch(
						'tags',
						queryset=Tag
						.objects
						.order_by('name')
						)
					)
				)