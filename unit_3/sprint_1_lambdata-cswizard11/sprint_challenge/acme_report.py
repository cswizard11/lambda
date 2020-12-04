from random import randint, sample, uniform
from acme import Product
 
# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']
 
 
def generate_products(num_products=30):
    products = [Product(name=ADJECTIVES[randint(0, len(ADJECTIVES) - 1)] + ' ' + NOUNS[randint(0, len(NOUNS) - 1)],
                        price=randint(5, 100),
                        weight=randint(5, 100),
                        flammability=uniform(0, 2.5))
                        for i in range(0, num_products)]
    # generate and add random products.
    return products
 
 
def inventory_report(products):
    # Loop over the products to calculate the report.
    names = []
    avg_price = 0
    avg_weight = 0
    avg_flammability = 0

    for i in products:
        if not(i.name in names):
            names.append(i.name)

        avg_price += i.price
        avg_weight += i.weight
        avg_flammability += i.flammability

    avg_price /= len(products)
    avg_weight /= len(products)
    avg_flammability /= len(products)

    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print('Unique product names:', len(names))
    print('Average price:', avg_price)
    print('Average weight:', avg_weight)
    print('Average flammability:', avg_flammability)


if __name__ == '__main__':
    inventory_report(generate_products())