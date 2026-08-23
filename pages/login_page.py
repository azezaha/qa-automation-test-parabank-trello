from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://parabank.parasoft.com/parabank/index.htm"
        
        # Locators Login
        self.username_input = page.locator('input[name="username"]')
        self.password_input = page.locator('input[name="password"]')
        self.login_btn = page.get_by_role("button", name="Log In")
        self.login_error_msg = page.get_by_text("An internal error has occurred and has been logged.")
        self.empty_error_msg = page.get_by_text("Please enter a username and password.")

        # Locators Links
        self.forgot_info_link = page.get_by_role("link", name="Forgot login info?")
        self.register_link = page.get_by_role("link", name="Register")
        
        # Locators Forgot Info Form
        self.customer_lookup_heading = page.get_by_role("heading", name="Customer Lookup")
        self.register_heading = page.get_by_role("heading", name="Signing up is easy!")

    def navigate(self):
        self.page.goto(self.url)

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_btn.click()

    def click_forgot_login(self):
        self.forgot_info_link.click()

    def click_register(self):
        self.register_link.click()

    def verify_lookup_page(self):
        expect(self.customer_lookup_heading).to_be_visible()

    def verify_register_page(self):
        expect(self.register_heading).to_be_visible()

