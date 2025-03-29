from scripts.candy_mapper import CandyMapper

def test_interact_with_more_dropdown_list(browser):
    candy = CandyMapper(browser)
    candy.open_candy_mapper()
    candy.interact_with_more_list()

    assert candy.interact_with_more_list()
