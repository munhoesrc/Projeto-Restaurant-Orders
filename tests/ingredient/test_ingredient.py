from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient = Ingredient('queijo mussarela')

    assert ingredient.name == 'queijo mussarela'

    excepted_restrictions = {
        Restriction.LACTOSE, Restriction.ANIMAL_DERIVED
    }
    assert ingredient.restrictions == excepted_restrictions

    assert repr(ingredient) == "Ingredient('queijo mussarela')"

    ingredient1 = Ingredient('queijo mussarela')
    assert ingredient == ingredient1

    assert hash(ingredient) == hash('queijo mussarela')

    ingredient2 = Ingredient("queijo parmesão")
    assert ingredient != ingredient2

    assert hash(ingredient) != hash(ingredient2)
