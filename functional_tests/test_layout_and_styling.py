from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
import unittest


class LayoutAndStyling(FunctionalTest):

    def test_layout_and_styling(self):
        # Ellie goes to the homepage
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)

        # She notices the input box is nicely centered
        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(
                inputbox.location['x'] + inputbox.size['width'] / 2,
                512, delta=10
        )

        # She starts a new list and sees the input is nicely centered there
        inputbox.send_keys('testing')
        inputbox.send_keys(Keys.ENTER)
        with self.wait_for_page_load(timeout=10):
            inputbox = self.get_item_input_box()
            self.assertAlmostEqual(
                    inputbox.location['x'] + inputbox.size['width'] / 2,
                    512, delta=10
            )


if __name__ == '__main__':
    unittest.main()

