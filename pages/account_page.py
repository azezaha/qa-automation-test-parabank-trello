from playwright.sync_api import Page, expect

class AccountPage:
    def __init__(self, page: Page):
        self.page = page
        
        # Locators Menu Navigasi Samping
        self.accounts_overview_heading = page.get_by_role("heading", name="Accounts Overview")
        self.account_table = page.locator("#accountTable")
        self.open_new_account_link = page.get_by_role("link", name="Open New Account")
        self.request_loan_link = page.get_by_role("link", name="Request Loan")
        self.logout_link = page.get_by_role("link", name="Log Out")

        # Locators Open Account
        self.account_type_select = page.locator("#type")
        self.from_account_select = page.locator("#fromAccountId")
        self.open_account_btn = page.get_by_role("button", name="Open New Account")
        self.account_opened_msg = page.get_by_text("Account Opened!")

        # Locators Request Loan
        self.loan_amount_input = page.locator("#amount")
        self.down_payment_input = page.locator("#downPayment")
        self.apply_loan_btn = page.get_by_role("button", name="Apply Now")
        self.loan_status = page.locator("#loanStatus")

    def verify_accounts_page(self):
        expect(self.accounts_overview_heading).to_be_visible()

    def open_new_account(self):
        self.open_new_account_link.click()
        self.from_account_select.wait_for(state="visible")
        self.page.wait_for_timeout(1000)
        self.account_type_select.select_option("1")
        self.open_account_btn.click()

    def verify_account_created(self):
        expect(self.account_opened_msg).to_be_visible()

    def apply_for_loan(self, amount, down_payment):
        self.request_loan_link.click()
        self.loan_amount_input.fill(amount)
        self.down_payment_input.fill(down_payment)
        self.apply_loan_btn.click()

    def verify_loan_submitted(self):
        expect(self.loan_status).to_be_visible()

    def logout(self):
        self.logout_link.click()