*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}               https://www.saucedemo.com/
${BROWSER}           Chrome
${NAME}              performance_glitch_user
${PASSWORD}          secret_sauce
${EXPECTED_TITLE}    Swag Labs
${CART}              xpath=//*[@id="shopping_cart_container"]/a
${CHECKOUT}          xpath=//*[@id="checkout"]
${TITLE}             Checkout: Your Information

*** Test Cases ***
Test Login To SauceDemo And Add To Cart
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Fill Login Inputs
    Click Button    xpath=//input[@id="login-button"]
    Wait Until Page Contains    ${EXPECTED_TITLE}    timeout=3s
    Click Button    //*[@id="add-to-cart-sauce-labs-backpack"]
    Click Button    //*[@id="add-to-cart-sauce-labs-onesie"]
    Click Button    //*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]
    Click Element    ${CART}
    Click Checkout Then Assert Buyer Info
    Close Browser

*** Keywords ***
Fill Login Inputs
    Input Text    id=user-name    ${NAME}
    Input Text    id=password    ${PASSWORD}

Click Checkout Then Assert Buyer Info
    Click Button            ${CHECKOUT}
    Page Should Contain     ${TITLE}
