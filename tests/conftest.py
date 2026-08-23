import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="function")
def context(playwright_instance):
    # Headless=True agar browser berjalan di latar belakang (ganti False jika ingin melihat browser terbuka)
    browser = playwright_instance.chromium.launch(headless=True)
    context = browser.new_context()
    # Merekam tracing untuk debugging jika pengujian gagal
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield context
    context.tracing.stop(path="trace.zip")
    context.close()
    browser.close()

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()