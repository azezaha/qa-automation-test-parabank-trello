import pytest
from pytest_bdd import scenarios, given, when, then
from pages.login_page import LoginPage
from pages.account_page import AccountPage

scenarios("../features/parabank.feature")

# --- GIVEN STEPS ---

@given("I open the ParaBank home page")
def open_parabank_home(page):
    login_page = LoginPage(page)
    login_page.navigate()
    return login_page

@given("I am logged into my ParaBank portal")
def login_to_portal(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("john", "demo")
    account_page = AccountPage(page)
    account_page.verify_accounts_page()
    return account_page

# --- WHEN STEPS ---

@when("I submit valid username and password")
def submit_valid_credentials(page):
    LoginPage(page).login("john", "demo")

@when("I attempt to log in with an invalid password")
def submit_invalid_password(page):
    LoginPage(page).login("john", "wrong_password_123")

@when("I submit the login form without entering any credentials")
def submit_empty_form(page):
    LoginPage(page).login("", "")

@when("I click on the forgot login info link")
def click_forgot_login(page):
    LoginPage(page).click_forgot_login()

@when("I click on the registration link")
def click_register(page):
    LoginPage(page).click_register()

@when("I submit a request to open a new savings account")
def step_open_account(page):
    AccountPage(page).open_new_account()

@when("I apply for a loan of 500 with 100 down payment")
def step_apply_loan(page):
    AccountPage(page).apply_for_loan("500", "100")

@when("I click on the Log Out link")
def click_logout_link(page):
    AccountPage(page).logout()

# --- THEN STEPS ---

@then("I should be redirected to the Accounts Overview page")
def verify_overview(page):
    AccountPage(page).verify_accounts_page()

@then("a verification error message should be displayed")
def verify_auth_error(page):
    LoginPage(page).login_error_msg

@then("I should see a prompt asking for username and password")
def verify_empty_error(page):
    LoginPage(page).empty_error_msg

@then("the Customer Lookup form should be displayed")
def verify_customer_lookup(page):
    LoginPage(page).verify_lookup_page()

@then("the Signing up is easy form should be displayed")
def verify_registration(page):
    LoginPage(page).verify_register_page()

@then("I should see confirmation that the account is opened")
def verify_account_open_success(page):
    AccountPage(page).verify_account_created()

@then("the loan request result status should be displayed")
def verify_loan_success(page):
    AccountPage(page).verify_loan_submitted()

@then("I should be returned to the home page with login panel visible")
def verify_home_login_panel(page):
    LoginPage(page).username_input