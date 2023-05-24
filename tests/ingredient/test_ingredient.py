from src.models.ingredient import Ingredient


def test_ingredient():
    ingrediente1 = Ingredient("salmão")
    ingrediente2 = Ingredient("abacaxi")
    ingrediente3 = Ingredient("queijo gorgonzola")

    assert ingrediente1.name == "salmão"
    assert ingrediente2.name == "abacaxi"
    assert ingrediente3.name == "queijo gorgonzola"

    assert ingrediente3 != ingrediente1
    assert ingrediente3 == ingrediente3

    assert hash(ingrediente3) == hash(ingrediente3)
    assert hash(ingrediente1) != hash(ingrediente3)

    assert repr(ingrediente3) == "Ingredient('queijo gorgonzola')"
    assert repr(ingrediente2) != "Ingredient('salmão')"

    assert ingrediente2.restrictions == set()
