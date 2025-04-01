*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}                    https://candymapper.com
${BROWSER}                Chrome
${POPUP_CLOSE_BUTTON}     id=popup-widget25042-cta
${LAUNCH_BUTTON}          xpath=//a[text() = 'Launch CandyMapper']
${EXPECTED_TITLE}         This spooky slow service takes forever to load...

*** Test Cases ***
Open CandyMapper And Verify Subpage Title
    Open Browser        ${URL}    ${BROWSER}
        options=add_argument("--headless"),
            add_argument("--disable-gpu"),
            add_argument("--no-sandbox"),
            add_argument("--disable-dev-shm-usage"),
            add_argument("--user-data-dir=/tmp/chrome-profile")
    Maximize Browser Window
    Wait Until Element Is Visible    ${POPUP_CLOSE_BUTTON}    timeout=5s
    Click Element       ${POPUP_CLOSE_BUTTON}
    Click Element       ${LAUNCH_BUTTON}
    Wait Until Page Contains    ${EXPECTED_TITLE}    timeout=5s
    Close Browser
