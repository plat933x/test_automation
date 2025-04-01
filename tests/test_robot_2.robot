*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}               https://www.saucedemo.com/
${BROWSER}           firefox
${NAME}              standard_user
${PASSWORD}          secret_sauce
${EXPECTED_TITLE}    Swag Labs

*** Test Cases ***
Test Login Into SauceDemo
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Fill Login Inputs
    Click Button    xpath=//input[@id="login-button"]
    Wait Until Page Contains    ${EXPECTED_TITLE}    timeout=5s
    Close Browser

*** Keywords ***
Close Popup If Present
    Run Keyword And Ignore Error    Click Element    xpath=//*[@id='popup-widget25042-cta']

Fill Login Inputs
    Input Text     id=user-name    ${NAME}
    Input Text     id=password    ${PASSWORD}
