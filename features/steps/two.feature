Feature:create a new account
  Scenario: Do a login with new account
    Given : launch the website
    When :  i am on the create account page
    Then : First "name" last "lname"
    And : close the broweser.

 Scenario Outline: testing with multiple account

   Given : launch the website
   When : i am on the create accoount page
   Then : enter <username> and <password>
   And : close the problems

   Examples:
    |username |password |
    |user1    |pass     |
    |user2    |pass     |
    |user3    |pass     |
