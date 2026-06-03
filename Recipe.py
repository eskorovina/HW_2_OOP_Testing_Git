class Recipe:
    def __init__(self, title: str, ingredients: list):
        self.title=title
        self.ingredients=ingredients

    def add_ingredient(self, ingredient: Ingredient):
        for product in self.ingredients:
            if product==ingredient:
                product.quantity +=ingredient.quantity
                return
        self.ingredients.append(ingredient)

    @static method
    def is_valid_ratio(ratio):
        try:
            return ratio>0
        except (ValueError, TypeError):
            return False

    def scale(self, ratio: float):
        if not Recipe.is_valid_ratio(ratio):
            raise ValueError("коэффицеиент должен быть >0")
        
        ratio_ingredients=[]
        for product in self.ingredients:
            new_quantity=product.quantity*ratio
            ratio_ingredients.append(Ingredient(product.name, new_quantity, product.unit))
    
        return Recipe(self.title, ratio_ingredients)

    def __len__(self):
        return len(self.ingredients)
    
    def __str__(self):
        result=f"{self.title}"
        for ingredient in self.ingredients:
            result+=f"\n {ingredient}"
        return result