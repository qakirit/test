
  Feature: Login feature
    Scenario: Login with valid creditionall
      Given : Launch the webbowser
      When : I am on the login page
      Then : entering the   "student" and "Password123"
      And : close the browser


    Scenario Outline: Checking with mulitple emaild id
      Given : Launch the webbowser
      When : I am on the login page
      Then : entering the   "<username>" and "<password>"
      And : close the browser

      Examples:
      |username |password |
      |user1    |pass     |
      |user2    |pass     |
      |user3    |pass     |


