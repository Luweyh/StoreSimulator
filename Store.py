class Product:
    """ Represents the products in the store """

    def __init__(self, product_id, title, description, price, quantity_available):
        """ Initializes important infor of the the product """
        self._product_id = product_id
        self._title = title
        self._description = description
        self._price = price
        self._quantity_available = quantity_available

    def get_product_id(self):
        """ Gets the product ID code"""
        return self._product_id

    def get_title(self):
        """ Gets the product title"""
        return self._title

    def get_description(self):
        """" Gets the product description """
        return self._description

    def get_price(self):
        """ Get the product price """
        return self._price

    def get_quantity_available(self):
        return self._quantity_available

    def decrease_quantity(self):
        """ Decreases quantity by one"""
        self._quantity_available -= 1
        return True


class Customer:
    """ Represent the customer in the store """

    def __init__(self, name, customer_id, is_premium_member):
        """ Initializes the name, customer ID and whether they are a premium member """
        self._name = name
        self._customer_id = customer_id
        self._is_premium_member = is_premium_member
        self._customer_cart = []

    def get_name(self):
        """ Gets the customer name """
        return self._name

    def get_customer_id(self):
        """ Gets the customer ID """
        return self._customer_id

    def get_customer_cart(self):
        """ Gets the customer cart"""
        return self._customer_cart

    def is_premium_member(self):
        """ returns the status of the premium member"""
        return self._is_premium_member

    def add_product_to_cart(self, product_id):
        """ Add product to the cart """
        self._customer_cart.append(product_id)

    def empty_cart(self):
        """ Empties the cart """
        self._customer_cart = []


class Store:
    """ Represent the Store """

    def __init__(self):
        self._store_inventory = []
        self._store_members = []

    def get_store_inventory(self):
        """ Gets the store inventory"""
        return self._store_inventory

    def get_store_members(self):
        """ gets the store members """
        return self._store_members

    def add_product(self, product):
        """ Adds the product to the store inventory """
        self._store_inventory.append(product)
        return True

    def add_member(self, customer):
        """ Adds the customer to the member list"""
        self._store_members.append(customer)
        return True

    def get_product_from_id(self, ID):
        """ Takes a product ID and returns the product"""
        for product in self._store_inventory:
            if product.get_product_id() == ID:
                return product

        return None  # When no product is found

    def get_member_from_id(self, ID):
        """ Takes a Customer ID and returns the customer with the matching ID """
        for customer in self._store_members:
            if customer.get_customer_id() == ID:
                return customer

        return None  # When no customer is found

    def product_search(self, search):
        """ Searches for a product ID based on the given search """

        # List for the searches found
        matches_found_in_search = []

        # Iterates through the store inventory
        for product in self._store_inventory:

            # checks to see if the search is in the title and add it to the list
            if search.lower() in product.get_title().lower():
                matches_found_in_search.append(product.get_product_id())

            # checks for the matching description and adds the ID to the list
            elif search.lower() in product.get_description().lower():
                matches_found_in_search.append(product.get_product_id())

        # sorts the list
        matches_found_in_search.sort()

        # returns the sorted list for the product search
        return matches_found_in_search

    def add_product_to_member_cart(self, product_id, customer_id):
        """ This adds the product to the member cart """

        # gets the customer from the ID
        product = self.get_product_from_id(product_id)

        # gets the customer from the ID
        customer = self.get_member_from_id(customer_id)

        # see if the product exist
        if product is None:
            return "product ID not found"

        # Sees if the customer is a member
        if customer is None:
            return "member ID not found"

        # Sees if the product is in stock
        if product.get_quantity_available() <= 0:
            return "product ouf of stock"

        # adds product to customer cart
        customer.add_product_to_cart(product_id)
        return "product added to cart"

    def check_out_member(self, customer_id):
        """ Checks the member out of the store with their items"""

        product_total = 0.00  # The cost of all products
        shipping_cost = 0.00  # the shipping charges

        # finds the customer based on ID
        customer = self.get_member_from_id(customer_id)

        # checks if ID does not match member of store
        if customer is None:
            raise InvalidCheckoutError()

        # iterates through the customer cart
        for product_id in customer.get_customer_cart():

            product = self.get_product_from_id(product_id)

            # finds the quantity available
            quantity = product.get_quantity_available()

            # If the product has at least 1 in stock
            if quantity > 1:
                product_total += product.get_price()        # gets the price of product
                product.decrease_quantity()                 # decreases the quantity

        # member pays 7% shipping cost if they are not premium member
        if customer.is_premium_member() is False:
            shipping_cost = product_total * 0.07

        # empties the customer's cart
        customer.empty_cart()

        # the grand total is the product cost plus the shipping cost
        grand_total = product_total + shipping_cost

        return grand_total


class InvalidCheckoutError(Exception):
    pass


def main():
    """ This to test the code above. This main functions tries to check out a member"""

    # creating the products
    p1 = Product("889", 'Rodent of unusual size', "when a rodent of the usual size just won't do", 33.45, 8)
    p2 = Product("510", 'hair', 'wash this carefully', 5, 6)

    # creating the customer
    c1 = Customer("Yinsheng", "QWF", False)

    myStore = Store()
    myStore.add_product(p1)     # adding product 1
    myStore.add_product(p2)     # adding product 2
    myStore.add_member(c1)      # adding customer

    try:
        myStore.check_out_member(c1.get_customer_id())  # trying checking out member

    except InvalidCheckoutError:        # when an Invalid checkout error happens.
        print("Customer ID not found")

if __name__ == "__main__":
    main()  # calling the main function