from Recipe import Recipe

class DietaryRecipe(Recipe):
    def __init__(self, title: str, diet_type: str, ingredients: list):
        super.__init__(title, ingredients)
        self.diet_type=diet_type


    def scale(self, ratio: float):
        scale_recipe = super.scale(ratio)
        return DietaryRecipe(scale_recipe.title, self.diet_type, scale_recipe.ingredients)
    

    def __str__(self):
        new_diet_recipe=f"{[self.diet_type]} {super().__str__()}"
    