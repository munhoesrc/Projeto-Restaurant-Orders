from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    pizza_pepperoni = Dish("Pizza", 42.90)
    assert pizza_pepperoni.name == "Pizza"
    assert repr(pizza_pepperoni) == "Dish('Pizza', R$42.90)"

    pizza_pepperoni_with_bord = Dish("Pizza", 42.90)
    assert pizza_pepperoni == pizza_pepperoni_with_bord
    assert hash(pizza_pepperoni) == hash(pizza_pepperoni_with_bord)

    pizza_pepperoni.add_ingredient_dependency(Ingredient("Molho de tomate"), 1)
    assert pizza_pepperoni.recipe.get(Ingredient("Molho de tomate")) == 1
    assert pizza_pepperoni.get_ingredients() == {Ingredient("Molho de tomate")}
    assert pizza_pepperoni.get_restrictions() == set()

    pizza_pepperoni.add_ingredient_dependency(Ingredient(
        "Queijo mussarela"
        ), 2)
    expected_ingredients = {
        Ingredient("Molho de tomate"), Ingredient("Queijo mussarela")
        }
    assert pizza_pepperoni.get_ingredients() == expected_ingredients
    assert pizza_pepperoni.get_restrictions() == set()

    egg_with_bacon = Dish("Ovo com bacon", 10.99)
    assert hash(pizza_pepperoni) != hash(egg_with_bacon)

    with pytest.raises(TypeError):
        Dish("name", "price")
    with pytest.raises(ValueError):
        Dish("name", 0)
