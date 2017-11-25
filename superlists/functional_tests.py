from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_star_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app.
        # he goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('FInish the test!')

        # She is invited to enter a to-do item right away

        # She types "buy peacock feather" into a text box

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" an item in a to-do list

        # There is still a text box inviting her to add other items
        # She enters "Use peacock feather to make a fly"

        # The age updates again, and now shows both items on her list

        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her - there is some
        # explanatory text to that effect

        # She visits that url - her to-do list is still there

        # Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main()
