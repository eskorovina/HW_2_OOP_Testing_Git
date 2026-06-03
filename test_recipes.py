import pytest
from classes.Ingredient import Ingredient
from classes.Recipe import Recipe
from classes.ShoppingList import ShoppingList

def test_ingredient():
    ingredient1 = Ingredient("Мука", 500.0, "г")
    ingredient2 = Ingredient("Мука", 300.0, "г")
    ingredient3 = Ingredient("Сахар", 200.0, "г")
    ingredient4 = Ingredient("Сахар", 200.0, "кг")
    assert ingredient1.name == "Мука"
    assert ingredient1.quantity == 500.0
    assert ingredient1.unit == "г"
    assert str(ingredient1) == "Мука: 500.0 г"
    assert ingredient1 == ingredient2
    assert ingredient1 != ingredient3
    assert ingredient3 != ingredient4

def test_recipe():
    ingredient1 = Ingredient("Яйцо", 2.0, "шт")
    ingredient2 = Ingredient("Молоко", 100.0, "мл")
    ingredient3 = Ingredient("Молоко", 200.0, "мл")

    recipe1 = Recipe("Омлет", [ingredient1, ingredient2])
    assert recipe1.title == "Омлет"
    assert recipe1.ingredients[1]== ingredient2
    recipe2=Recipe("Торт", [])
    recipe2.add_ingredient(ingredient2)
    assert recipe2.ingredients[0]==ingredient2
    recipe2.add_ingredient(ingredient3)
    assert recipe2.ingredients[0].quantity == 300.0
    big_recipe1 = recipe1.scale(4)
    assert big_recipe1 != recipe1
    assert big_recipe1.ingredients[0].quantity == 8.0
    assert big_recipe1.ingredients[1].quantity == 400.0
    assert recipe1.ingredients[0].quantity == 2.0

    with pytest.raises(ValueError, match="коэффициент должен быть >0"):
        recipe2.scale(-1)
    
    assert len(recipe1) == 2

def test_shopping_list():
    recipe1 = Recipe("Хлеб", [
        Ingredient("Мука", 500.0, "г")])
    
    recipe2 = Recipe("Блины", [
        Ingredient("Мука", 200.0, "г"),
        Ingredient("Молоко", 300.0, "мл")])
    
    shopping_list = ShoppingList()

    shopping_list.add_recipe(recipe1, 2)
    ing, tit = shopping_list._items[0]
    assert ing.quantity == 1000.0
    assert ing.name == "Мука"
    assert tit == "Хлеб"

    with pytest.raises(ValueError, match="Количество порций должно быть положительным"):
        shopping_list.add_recipe(recipe1, 0)
    
    shopping_list.add_recipe(recipe2, 3)
    shopping_list.remove_recipe("Хлеб")

    assert len(shopping_list._items) == 1
    assert shopping_list._items[0][1]=="Блины"

    shopping_list.remove_recipe("Бургер")
    assert len(shopping_list._items) == 1


    shopping_list2 = ShoppingList()
    recipe3 = Recipe("Булочка", [Ingredient("Мука", 500.0, "г")])
    recipe4 = Recipe("Пицца", [Ingredient("Мука", 300.0, "г")])

    shopping_list2.add_recipe(recipe3, 1)
    shopping_list2.add_recipe(recipe4, 1)
    result = shopping_list2.get_list()

    assert len(result) == 1
    assert result[0].name == "Мука"
    assert result[0].quantity == 800
    assert result[0].unit == "г"

    shopping_list3 = ShoppingList()
    recipe5 = Recipe("Суп", [
        Ingredient("Картошка", 3.0, "шт"),
        Ingredient("Морковь", 1.0, "шт"),
        Ingredient("Лук", 0.5, "шт")])
    
    shopping_list3.add_recipe(recipe5, 1)

    result = shopping_list3.get_list()
    names = [ingredient.name for ingredient in result]
    assert names == sorted(names)

    list1 = ShoppingList()
    list2 = ShoppingList()
    ing1 = Ingredient("Мука", 500, "г")
    ing2 = Ingredient("Яйцо", 2, "шт")

    recipe1 = Recipe("Пирог", [ing1])
    recipe2 = Recipe("Яичница", [ing2])

    list1.add_recipe(recipe1, 1)
    list2.add_recipe(recipe2, 2)

    combo = list1 + list2

    assert len(list1._items) == 1
    assert len(list2._items) == 1

    assert len(combo._items) == 2
    assert combo!=list1
    assert combo!=list2