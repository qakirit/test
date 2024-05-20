*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://practice.expandtesting.com/login
${browser}    Firefox

*** Test Cases ***
Successful Login Test
    Open Browser    ${url}    ${browser}
    Maximize Browser Window


    Input Text     id=username  tes
    Input Text     id=password  Hello, world!


    Click Button     Login
    Page Should Contain    Dashboard

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
