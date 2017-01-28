from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
import unittest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Ellie goes to the home page and accidentally tries to submit an
        # empty list item. She hits Enter on the empty inputbox
        self.browser.get(self.server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys(Keys.ENTER)

        # The homepage refreshes and there is an error message saying that the
        # list items cannot be blank
        error = self.browser.find_element_by_css_selector('.has-error')
        with self.wait_for_page_load(timeout=10):
            self.assertEqual(error.text, "You can't have an empty list item")

        # She tries again with some text for the new item which now works
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        with self.wait_for_page_load(timeout=10):
            self.check_for_row_in_list_table('1: Buy milk')

        # Perversely she now decides to submit a second blank list item
        inputbox.send_keys(Keys.ENTER)

        # She receives a similar warning on the list page
        error = self.browser.find_element_by_css_selector('.has-error')
        with self.wait_for_page_load(timeout=10):
            self.assertEqual(error.text, "You can't have an empty list item")

        # And she can correct it by filling some text in
        inputbox.send_keys('Make tea')
        inputbox.send_keys(Keys.ENTER)
        with self.wait_for_page_load(timeout=10):
            self.check_for_row_in_list_table('1: Buy milk')
            self.check_for_row_in_list_table('2: Make tea')


if __name__ == '__main__':
    unittest.main()

