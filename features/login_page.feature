Feature: Login To SauceDemo

  Scenario: Successful login to saucedemo webpage
    Given SauceDemo URL loaded
    When Username and password entered
    And Login button clicked
    Then Dashboard for logged users shall be visible
