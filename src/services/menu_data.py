# Req 3
import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = self.load_menu_data(source_path)

    def load_menu_data(self, source_path: str) -> set:
        dishes = set()

        with open(source_path) as file:
            reader = csv.reader(file)
            header, *data = reader

            for item in data:
                name, price, ingredient_name, quantity = item[:4]

                dish = self.get_or_create_dish(dishes, name, float(price))
                ingredient = Ingredient(ingredient_name)
                dish.add_ingredient_dependency(ingredient, int(quantity))

        return dishes

    def get_or_create_dish(
            self, dishes: set, name: str, price: float) -> Dish:
        for dish in dishes:
            if dish.name == name:
                return dish

        new_dish = Dish(name, price)
        dishes.add(new_dish)
        return new_dish
