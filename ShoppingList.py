class ShoppingList:
    def __init__(self):
        self._items = []
    
    def add_recipe(recipe: Recipe, portions: float):
        if portions<=0:
            raise ValueError("Количество порций должно быть положительным")
        scale_recipe = recipe.scale(portions)
        for ingredient in scale_recipe.ingredients:
            self._items.append((ingredient, recipe.title))
    def remove_recipe(self, title: str):
        self._items=[pair for pair in self._items if pair[1]!=title]
    

    def get_list(self):

        ingredient_dict={}
        for pair in self._items:
            key=(pair[0].name, pair[0].unit)
            ingredient_dict[key] = ingredient_dict.get(key, 0)+pair[0].quantity

        result = [Ingredient(name, quantity, unit) for (name, unit), quantity in ingredient_dict.items()]
        result.sort(key=lambda ingredient: ingredient.name)
        
        return result
    
    def __add__(self, other: ShoppingList):
        new_shopping_list=ShoppingList()
        new_shopping_list._items = self._items+other._items
        return new_shopping_list
