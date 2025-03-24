test_dict = {
  "brand": "Ford",
  "model": "Mustang GT",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

def test_ford_dict():
    assert test_dict.get("brand") == "Ford"
    assert test_dict.get("colors") == ["red", "white", "blue"]
    assert not test_dict["year"] == 1999

def test_new_dict():
    test_dict.update({"brand": "Opel"})
    assert test_dict.get("brand") == "Opel"