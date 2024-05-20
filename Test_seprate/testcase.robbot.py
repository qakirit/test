*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BROWSER}    Chrome
${URL}        https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

*** Test Cases ***
Successful Login Test
    Open Browser    ${URL}    ${BROWSER}
    Input Text    username_field    ${VALID_USERNAME}
    Input Text    password_field    ${VALID_PASSWORD}
    Click Button    login_button
    Page Should Contain    Welcome, User!

Unsuccessful Login Test
    Open Browser    ${URL}    ${BROWSER}
    Input Text    username_field    ${INVALID_USERNAME}
    Input Text    password_field    ${INVALID_PASSWORD}
    Click Button    login_button
    Page Should Contain    Invalid username or password

*** Keywords ***
Input Text
    [Arguments]    ${locator}    ${text}
    Input Text    ${locator}    ${text}

Click Button
    [Arguments]    ${locator}
    Click Element    ${locator}
