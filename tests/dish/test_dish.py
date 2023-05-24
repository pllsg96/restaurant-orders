from src.models.dish import Dish
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():

    with pytest.raises(TypeError):
        Dish("Lasanha", "20.99")

    with pytest.raises(ValueError):
        Dish("Lasanha", -20.99)

    menu1 = Dish("Lasanha", 20.99)
    menu2 = Dish("Hamburguer", 10.99)
    menu3 = Dish("Lasanha", 20.99)

    assert menu1.name == "Lasanha"
    assert menu1.price == 20.99
    assert menu1 != menu2
    assert menu1 == menu3
    assert hash(menu1) == hash(menu1)
    assert hash(menu1) != hash(menu2)

    ingrediente1 = Ingredient("Queijo")
    ingrediente2 = Ingredient("Alface")
    menu2.add_ingredient_dependency(ingrediente1, 2)
    menu2.add_ingredient_dependency(ingrediente2, 2)
    assert ingrediente1 in menu2.recipe
    assert menu2.recipe[ingrediente1] == 2
    assert ingrediente2 in menu2.recipe
    assert menu2.recipe[ingrediente2] == 2
    
    ingrediente1.restrictions = {"Lactose"}
    ingrediente2.restrictions = {"Vegano"}
    restrictions = menu2.get_restrictions()
    assert "Lactose" in restrictions

    ingredients = menu2.get_ingredients()
    assert ingrediente1 in ingredients
    assert ingrediente2 in ingredients

    menuError = Dish("Maç@", 6.66)
    assert repr(menuError) == "Dish('Maç@', R$6.66)"
