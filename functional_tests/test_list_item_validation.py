from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
import unittest
from time import sleep


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Ellie goes to the home page and accidentally tries to submit an
        # empty list item. She hits Enter on the empty input box.
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)

        # The browser intercepts the request and does not load the list page.
        self.assertNotIn(
                "Buy milk",
                self.browser.find_element_by_tag_name('body').text
                )

        # She tries again with some text for the new item which now works
        self.get_item_input_box().send_keys('Buy milk')
        self.get_item_input_box().send_keys(Keys.ENTER)
        with self.wait_for_page_load(timeout=10):
            self.check_for_row_in_list_table('1: Buy milk')

        # Perversely she now decides to submit a second blank list item
        self.get_item_input_box().send_keys(Keys.ENTER)

        # Again, the browser will not comply
        self.check_for_row_in_list_table('1: Buy milk')
        rows = self.browser.find_elements_by_css_selector('#id_list_table tr')
        self.assertEqual(len(rows), 1)

        # And she can correct it by filling some text in
        self.get_item_input_box().send_keys('Make tea')
        self.get_item_input_box().send_keys(Keys.ENTER)
        with self.wait_for_page_load(timeout=10):
            self.check_for_row_in_list_table('1: Buy milk')
            self.check_for_row_in_list_table('2: Make tea')


if __name__ == '__main__':
    unittest.main()

