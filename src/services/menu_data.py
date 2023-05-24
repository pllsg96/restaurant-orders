from src.models.dish import Dish
from src.models.ingredient import Ingredient
import csv


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.items = self.r_file(source_path)
        self.dishes = self.generate_menu()

    def r_file(self, path: str):
        with open(path, "r") as file:
            menu = csv.DictReader(file)
            return list(menu)

    def generate_menu(self):
        menu = {}
        for item in self.items:
            dish = Dish(item["dish"], float(item["price"]))
            ingredient = Ingredient(item["ingredient"])
            amount = int(item["recipe_amount"])
            if dish not in menu:
                menu[dish] = dish
            menu[dish].add_ingredient_dependency(
                ingredient, amount
            )
        return set(menu.values())
