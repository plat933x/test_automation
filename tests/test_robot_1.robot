*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}                    https://candymapper.com
${BROWSER}                Chrome
${USER-DATA-DIR}          options=add_argument("--user-data-dir=/tmp/chrome-profile")
${POPUP_CLOSE_BUTTON}     id=popup-widget25042-cta
${LAUNCH_BUTTON}          xpath=//a[text() = 'Launch CandyMapper']
${EXPECTED_TITLE}         This spooky slow service takes forever to load...

*** Test Cases ***
Open CandyMapper And Verify Subpage Title
    Open Browser        ${URL}    ${BROWSER}    ${USER-DATA-DIR}
    Maximize Browser Window
    Wait Until Element Is Visible    ${POPUP_CLOSE_BUTTON}    timeout=5s
    Click Element       ${POPUP_CLOSE_BUTTON}
    Click Element       ${LAUNCH_BUTTON}
    Wait Until Page Contains    ${EXPECTED_TITLE}    timeout=5s
    Close Browser
