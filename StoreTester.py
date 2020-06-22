class StoreTester(unittest.TestCase):
    """ Contain unit tests for the Store Class """

    def test_product_methods(self):
        """ This test the methods in the Product Class """

        # create an object to test
        apple = Product('555', 'apple', 'sweet fruit', 1, 10)

        self.assertEqual(apple.get_product_id(), '555')  # verify correct product ID
        self.assertEqual(apple.get_title(), 'apple')  # verify correct title
        self.assertEqual(apple.get_description(), 'sweet fruit')  # verify correct description
        self.assertEqual(apple.get_price(), 1)  # verify correct price
        self.assertEqual(apple.get_quantity_available(), 10)  # verify correct quantity

        apple.decrease_quantity()  # verify if decrease quantity works
        apple.decrease_quantity()

        # this should decrease quantity by 2
        self.assertEqual(apple.get_quantity_available(), 8)

    def test_customer_methods(self):
        """ Test the methods in the Customer class """

        # create a customer object to test
        customer_1 = Customer('John', '449', False)

        self.assertEqual(customer_1.get_name(), 'John')  # test if correct name
        self.assertEqual(customer_1.get_customer_id(), '449')  # test if correct customer ID
        self.assertEqual(customer_1.is_premium_member(), False)  # test if premium is correct

        self.assertFalse(customer_1.is_premium_member())  # test premium is false

        # create a product object to test
        orange = Product("321", "Orange", "Like the color", 1, 888)

        # Testing if adding a product to the cart is done correct
        orange_id = orange.get_product_id()
        customer_1.add_product_to_cart(orange_id)
        self.assertIn(orange_id, customer_1.get_customer_cart())

    def test_adding_product_to_inventory(self):
        """ Test if adding product to inventory works """

        apple = Product('555', 'apple', 'sweet fruit', 1, 10)
        store = Store()
        store.add_product(apple)
        self.assertIn(apple, store.get_store_inventory())  # apple should be in the store inventory

    def test_adding_members(self):
        """ test if adding members work """

        customer_1 = Customer('John', '449', False)
        store = Store()
        store.add_member(customer_1)  # finding member by ID
        self.assertIn(customer_1, store.get_store_members())  # customer_1 should be one of the store members

    def test_product_search(self):
        """ Test if product search works """

        apple = Product('555', 'apple', 'sweet fruit', 1, 10)

        store = Store()
        store.add_product(apple)  # adding the product

        # product search should return a list of product ID
        self.assertEqual(store.product_search('apple'), ['555'])

        # product search should return ID only and not the title
        self.assertNotIn('apple', store.product_search('apple'))

    def test_checking_out_member_and_calculations(self):
        """ Checking out a member cart with accurate calculations  """

        apple = Product('555', 'apple', 'sweet fruit', 1, 10)
        orange = Product('444', 'orange', 'like the color', 2, 10)
        customer_1 = Customer('John', '449', False)
        store = Store()
        store.add_member(customer_1)  # adding customer to store
        store.add_product(apple)  # adding apple product to store
        store.add_product(orange)  # adding orange product to store

        store.add_product_to_member_cart('555', '449')  # adding apple to customer_1 cart
        store.add_product_to_member_cart('444', '449')  # adding orange to customer_1 cart

        # this finds the grand total for this customer which should be 3.21 since
        # (2 + 1 ) * 1.07 = 3.21 which is the product cost plus the shipping cost
        self.assertAlmostEqual(store.check_out_member('449'), 3.21, 2)

        # the cart should now be empty once the customer checks out
        self.assertEqual(customer_1.get_customer_cart(), [])


if __name__ == '__main__':
    unittest.main()