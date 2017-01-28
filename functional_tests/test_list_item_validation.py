from .base import FunctionalTest
import unittest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Ellie goes to the home page and accidentally tries to submit an
        # empty list item. She hits Enter on the empty inputbox

        # The homepage refreshes and there is an error message saying that the
        # list items cannot be blank

        # She tries again with some text for the new item which now works

        # Perversely she now decides to submit a second blank list item

        # She receives a similar warning on the list page

        # And she can correct it by filling some text in
        self.fail('write me')


if __name__ == '__main__':
    unittest.main()
