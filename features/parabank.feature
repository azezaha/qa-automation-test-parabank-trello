Feature: ParaBank Account and Transaction Services
  As a customer of ParaBank
  I want to access banking services
  So that I can manage my accounts, open new products, and apply for loans

  @smoke @login
  Scenario: Customer successfully signs in with valid credentials
    Given I open the ParaBank home page
    When I submit valid username and password
    Then I should be redirected to the Accounts Overview page

  @negative @login
  Scenario: Access is rejected when using an incorrect password
    Given I open the ParaBank home page
    When I attempt to log in with an invalid password
    Then a verification error message should be displayed

  @negative @login
  Scenario: Login form validation triggers when fields are left blank
    Given I open the ParaBank home page
    When I submit the login form without entering any credentials
    Then I should see a prompt asking for username and password

  @navigation
  Scenario: Customer can access the password recovery page
    Given I open the ParaBank home page
    When I click on the forgot login info link
    Then the Customer Lookup form should be displayed

  @navigation
  Scenario: Visitor can navigate to the registration form
    Given I open the ParaBank home page
    When I click on the registration link
    Then the Signing up is easy form should be displayed

  @functional @account
  Scenario: Authenticated user can open a new savings account
    Given I am logged into my ParaBank portal
    When I submit a request to open a new savings account
    Then I should see confirmation that the account is opened

  @functional @loan
  Scenario: Authenticated user can submit a loan application
    Given I am logged into my ParaBank portal
    When I apply for a loan of 500 with 100 down payment
    Then the loan request result status should be displayed

  @smoke @session
  Scenario: Authenticated user can log out safely
    Given I am logged into my ParaBank portal
    When I click on the Log Out link
    Then I should be returned to the home page with login panel visible