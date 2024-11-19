from pet import Pet
import pytest

def test_pet_instantiation():
    pet = Pet("Fido", "Dog", 3)
    assert pet.name == "Fido"
    assert pet.species == "Dog"
    assert pet.age == 3

def test_describe_method(capsys):
    pet = Pet("Fido", "Dog", 3)
    pet.describe()
    captured = capsys.readouterr()
    assert captured.out.strip() == "This is Fido, a Dog who is 3 years old."

def test_celebreate_birthday_method(capsys):
    pet = Pet("Fido", "Dog", 3)
    pet.celebrate_birthday()
    assert pet.age == 4
    captured = capsys.readouterr()
    assert captured.out.strip() == "Happy Birthday Fido! You are now 4 years old!"