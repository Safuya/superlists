from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(FunctionalTest):

    def test_can_start_list_for_one_user(self):
        # Ellie has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get(self.server_url)

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),
                         'Enter a to-do item')

        # She types "Buy peacock feathers" into a text box (Ellie's hobby
        # is tying fly-fishing lures
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates and now the page lists
        # "1: Buy peacock feathers to make a fly" as an item in the to-do list
        inputbox.send_keys(Keys.ENTER)
        with self.wait_for_page_load(timeout=10):
            self.check_for_row_in_list_table('1: Buy peacock feathers')

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Ellie is very
        # methodical)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again and now shows both items on her list
        with self.wait_for_page_load(timeout=10):
            self.check_for_row_in_list_table('1: Buy peacock feathers')
            self.check_for_row_in_list_table(
                 '2: Use peacock feathers to make a fly'
            )

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Ellie starts a new todo list
        self.browser.get(self.server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        with self.wait_for_page_load(timeout=10):
            self.check_for_row_in_list_table('1: Buy peacock feathers')

        # She notices that her list has a unique URL
        ellie_list_url = self.browser.current_url
        self.assertRegex(ellie_list_url, '/lists/.+')

        # Now a new user called Frank comes along to the site
        # Frank uses a browser on a different computer to Ellie
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Frank visits the homepage. There's no sign on Ellie's list
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Frank starts a new list by entering a new item. He is less
        # interesting than Ellie.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        with self.wait_for_page_load(timeout=10):
            self.check_for_row_in_list_table('1: Buy milk')

        # Frank gets his own unique URL
        frank_list_url = self.browser.current_url
        self.assertRegex(frank_list_url, '/lists/.+')

        # There's still no trace of Ellie's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        # Satisfied, they both go back to sleep


if __name__ == '__main__':
    unittest.main()

