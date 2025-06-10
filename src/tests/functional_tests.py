"""
Functional tests to test the user journey through the application.
"""
from django.test import LiveServerTestCase
from pytest_django.asserts import assertContains
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class UserJourneyTest(LiveServerTestCase):
    def setUp(self):
        firefox_options = Options()
        firefox_options.add_argument("--headless")  # Run in headless mode
        self.browser = webdriver.Firefox(options=firefox_options)
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.quit()

    def test_base_page_displays_correct_title(self):
        response = self.client.get('/')  # Use Django test client to get the base page
        assertContains(response, '<title>Base page</title>', status_code=200,
                       msg_prefix='Base page should display the correct title')
