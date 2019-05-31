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


    def test_types(self):
        prod = Product('Test 3')
        assert(type(prod.price) == int)

    def test_default_num_products(self):
        prods = generate_products()
        self.assertEqual(len(prods), 30)

    def test_legal_names(self):
        prods = generate_products()
        NOUNS = [['Anvil'], ['Catapult'], ['Disguise'], ['Mousetrap'], ['???']]
        ADJECTIVES = [['Awesome'], ['Shiny'], ['Impressive'], ['Portable'], ['Improved']]
        for p in prods:
            assert(p.name.split()[0] in x for x in ADJECTIVES)
            assert(p.name.split()[1] in x for x in NOUNS)


if __name__ == '__main__':
    unittest.main()
