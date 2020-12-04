import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS
 
 
class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def setUp(self):
        '''make the Product to use for testing'''
        self.test_prod = Product('Anvil', price=150, weight=2500, flammability=0.001)

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_attributes(self):
        '''test all default attributes'''
        prod = Product('Foobar')
        self.assertEqual(prod.price, 10)
        self.assertEqual(prod.weight, 20)
        self.assertEqual(prod.flammability, 0.5)

    def test_methods(self):
        '''test stealability and explode methods'''
        self.assertEqual(self.test_prod.stealability(), 'Not so stealable...')
        self.assertEqual(self.test_prod.explode(), '..fizzle.')

class AcmeReportTests(unittest.TestCase):
    '''make sure the acme reports are filed correctly'''
    def test_default_num_products(self):
        '''test that the default for generate_products() is 30'''
        products = generate_products()
        self.assertEqual(len(products), 30)

    def test_legal_names(self):
        '''test that the generated names are legal names'''
        possibilities = []
        for i in ADJECTIVES:
            for j in NOUNS:
                possibilities.append(i + ' ' + j)

        products = generate_products()
        for i in products:
            self.assertIn(i.name, possibilities)
 
 
if __name__ == '__main__':
    unittest.main()