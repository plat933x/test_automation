from scripts.candy_mapper import CandyMapper

def test_successful_open_url(browser):

    candy = CandyMapper(browser)
    candy.open_candy_mapper()

    # Image after pop up visible
    assert candy.is_image_visible() == True

def test_reach_home_tab(browser):

    candy = CandyMapper(browser)
    candy.open_candy_mapper()
    candy.go_to_home_tab()

    assert candy.go_to_home_tab() == True

def test_reach_halloween_tab(browser):

    candy = CandyMapper(browser)
    candy.open_candy_mapper()
    candy.go_to_halloween_tab()

    assert candy.go_to_halloween_tab() == True