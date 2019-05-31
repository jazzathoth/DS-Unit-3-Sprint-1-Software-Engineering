#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
        self.assertEqual(prod.weight, 20)


    """Test explosion and stealibility"""
    def test_functions(self):
        prod = Product('Test 2', 20, 20, 3)
        self.assertEqual(prod.explode(), '...BABOOM!!')
        self.assertEqual(prod.stealability(), 'Very stealable.')

if __name__ == '__main__':
    unittest.main()
