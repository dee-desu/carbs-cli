import pytest
from carbs.carbs import Nutritions

#Testing methods
def test_str():
    carbs = Nutritions()
    actual = str(carbs)
    expected = "welcome from Nutritions class" 
    assert actual == expected 

def test_repr():
    carbs = Nutritions()
    actual = repr(carbs)
    expected = "Nutritions class"
    assert actual == expected 

def test_max_carbs():
    max_carbs = Nutritions()
    max_carbs.set_carb(100,119)
    max_carbs.get_data()
    actual = max_carbs.max_carb
    expected = 119
    assert actual == expected 

def test_min_carbs():
    min_carbs= Nutritions()
    min_carbs.set_carb(100,119)
    min_carbs.get_data()
    actual = min_carbs.min_carb
    expected = 100
    assert actual == expected 
def test_response():
    response = Nutritions()
    response.set_carb(55,99)
    response.get_data()
    actual = len(response.r)
    expected = 10 
    assert actual == expected
def test_api_key():
    api_key = Nutritions()
    actual = api_key.api_key
    expected = "889e7e736f474d9a98442f1a93990afa" 
    assert actual == expected  
def test_min_and_max():
    
    with pytest.raises(ValueError): Nutritions().set_carb(100,50)
    

def test_url():
    url= Nutritions()
    url.set_carb(100,119)
    url.get_data()
    actual = url.url
    expected ="https://api.spoonacular.com/recipes/findByNutrients?apiKey=889e7e736f474d9a98442f1a93990afa&minCarbs=100&maxCarbs=119"
    assert actual == expected 