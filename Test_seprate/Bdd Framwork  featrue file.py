Feature: Testing with Parameter

  Scenario: Login with Parameter
    Given Launch the Browser
    When  Open the login page
    And  enter the username "student" and Password "Password123"
    And  clicking on the submit button
    Then login successful

Scenario Outline: Login with Multiple parameters
    Given Launch the Browser
    When Open the login page
    And enter the username "<username>" and Password "<password>"
    And clicking on the submit button
    Then login successful

Examples:
    | username | password   |
    | user1    | pass123    |
    | user2    | pass456    |
    | user3    | pass789    |
