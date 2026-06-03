import pytest
from classes.ingredient import Ingredient
from classes.recipe import Recipe
from classes.shoppingList import ShoppingList

def test_ingredient_1():
    ing = Ingredient("Мука", 500.0, "г")
    assert ing.name == "Мука"
    assert ing.quantity == 500.0
    assert ing.unit == "г"

def test_ingredient_2():
    ing = Ingredient("Мука", 500.0, "г")
    assert str(ing) == "Мука: 500.0 г"

def test_ingredient_3():
    ing1 = Ingredient("Мёд", 500.0, "г")
    ing2 = Ingredient("Мёд", 300.0, "г")
    ing3 = Ingredient("Сахар", 200.0, "г")
    ing4 = Ingredient("Мёд", 500.0, "кг")
    assert ing1 == ing2
    assert ing1 != ing3
    assert ing1 != ing4
    with pytest.raises(ValueError, match="Количество должно быть положительным"):
        Ingredient("Мука", -100.0, "г")


def test_recipe_1():
    ing = Ingredient("Яйцо", 2.0, "шт")
    recipe = Recipe("Яичница", [ing])
    assert recipe.title == "Яичница"

    assert len(recipe.ingredients) == 1
    assert recipe.ingredients[0] == ing

def test_recipe_2():
    recipe = Recipe("Блины", [])
    ing = Ingredient("Молоко", 200.0, "мл")
    recipe.add_ingredient(ing)

    assert len(recipe) == 1
    assert recipe.ingredients[0].quantity == 200.0

def test_recipe_3():
    recipe = Recipe("Яйцо в скорлупе", [])
    ing1 = Ingredient("Яйцо", 2.0, "шт")
    ing2 = Ingredient("Яйцо", 1.0, "шт")
    recipe.add_ingredient(ing1)
    recipe.add_ingredient(ing2)

    assert len(recipe) == 1
    assert recipe.ingredients[0].quantity == 3.0

def test_recipe_4():
    ing = Ingredient("Мука", 500.0, "г")
    recipe = Recipe("Хлеб", [ing])
    scal = recipe.scale(2)

    assert scal != recipe
    assert scal.title == recipe.title
    assert scal.ingredients[0].quantity == 1000.0
    assert recipe.ingredients[0].quantity == 500.0
    with pytest.raises(ValueError, match="коэффициент должен быть >0"):
        recipe.scale(-1)


def test_recipe_5():
    recipe = Recipe("Салат", [])
    recipe.add_ingredient(Ingredient("Огурец", 2.0, "шт"))
    recipe.add_ingredient(Ingredient("Помидор", 3.0, "шт"))
    assert len(recipe) == 2

    recipe.add_ingredient(Ingredient("Огурец", 1.0, "шт"))
    assert len(recipe) == 2



def test_shopping_list_1():
    recipe = Recipe("Пирог", [Ingredient("Тесто", 500.0, "г")])
    shopping_list = ShoppingList()
    shopping_list.add_recipe(recipe, 2)

    assert len(shopping_list._items) == 1

    ing, title = shopping_list._items[0]

    assert ing.quantity == 1000.0
    assert ing.name == "Тесто"
    assert title == "Пирог"
    with pytest.raises(ValueError, match="Количество порций должно быть положительным"):
        shopping_list.add_recipe(recipe, 0)


def test_shopping_list_2():


    recipe1 = Recipe("Чай", [Ingredient("Заварка", 5.0, "мл")])
    recipe2 = Recipe("Блины", [Ingredient("Мука", 200.0, "г"), Ingredient("Молоко", 300.0, "мл")])
    shopping = ShoppingList()

    shopping.add_recipe(recipe1, 1)
    shopping.add_recipe(recipe2, 1)

    assert len(shopping._items) == 3

    shopping.remove_recipe("Чай")
    assert len(shopping._items) == 2

    for ing, title in shopping._items:
        assert title == "Блины"
    
    shopping.remove_recipe("Сосиски в тесте")
    assert len(shopping._items) == 2


def test_shopping_list_3():
    recipe1 = Recipe("Пирожки", [Ingredient("Мука", 500.0, "г")])
    recipe2 = Recipe("Пирог", [Ingredient("Мука", 1000.0, "г")])
    shopping = ShoppingList()

    shopping.add_recipe(recipe1, 1)
    shopping.add_recipe(recipe2, 1)
    result = shopping.get_list()

    assert len(result) == 1
    assert result[0].name == "Мука"
    assert result[0].quantity == 1500.0
    assert result[0].unit == "г"

def test_shopping_list_4():
    recipe = Recipe("Суп", [
        Ingredient("Картошка", 3.0, "шт"),
        Ingredient("Морковь", 1.0, "шт"),
        Ingredient("Лук", 0.5, "шт")])
    

    shopping = ShoppingList()
    shopping.add_recipe(recipe, 1)
    result = shopping.get_list()
    names = [ing.name for ing in result]

    assert names == sorted(names)

def test_shopping_list_5():

    list1 = ShoppingList()
    list2 = ShoppingList()

    recipe1 = Recipe("Лимонад", [Ingredient("Лимон", 5.0, "шт")])
    recipe2 = Recipe("Морс", [Ingredient("Брусника", 200.0, "г")])
    
    list1.add_recipe(recipe1, 1)
    list2.add_recipe(recipe2, 2)
    combo = list1 + list2

    assert len(list1._items) == 1
    assert len(list2._items) == 1

    assert len(combo._items) == 2
    assert combo != list1
    assert combo != list2