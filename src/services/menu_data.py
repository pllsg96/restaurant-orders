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
            prato = Dish(item["dish"], float(item["price"]))
            ingredientes = Ingredient(item["ingredient"])
            valor = int(item["recipe_amount"])
            if prato not in menu:
                menu[prato] = prato
            menu[prato].add_ingredient_dependency(
                ingredientes, valor
            )

        return set(menu.values())
