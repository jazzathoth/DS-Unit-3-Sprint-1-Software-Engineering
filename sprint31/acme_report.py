#! /usr/bin/env python


from random import randint, sample, uniform
from acme import Product


# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    """Instantiates a list of 30 products and returns list"""
    products = []
    for x in range(num_products):
        products.append(Product("{} {}".format(sample(ADJECTIVES, 1),
                                sample(NOUNS, 1)),
                                randint(1, 50),
                                randint(1, 50),
                                uniform(0, 1)))
    return(products)


def inventory_report(products):
    """Creates a report of products by looping through
    a list of products, collecting attributes, then printing
    averages and counts of attributes"""
    names = []
    n_unique = []
    x_unique = 0
    prices = []
    weights = []
    flammability = []

    for product in products:
        names.append(product.name)
        prices.append(product.price)
        weights.append(product.weight)
        flammability.append(product.flammability)

    for n in names:
        if n not in n_unique:
            n_unique.append(n)
            x_unique += 1

    print('ACME CORPORATION INVENTORY REPORT')
    print('Unique product names: {}'.format(x_unique))
    print('Average price: {}'.format(sum(prices)/len(prices)))
    print('Average weight: {}'.format(sum(weights)/len(weights)))
    print('Average flammability: {}'
          .format(sum(flammability)/len(flammability)))

    pass  # TODO - your code! Loop over the products to calculate the report.


if __name__ == '__main__':
    inventory_report(generate_products())
