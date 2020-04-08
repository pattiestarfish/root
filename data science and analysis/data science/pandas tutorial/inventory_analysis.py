import pandas as pd

inventory = pd.read_csv('inventory.csv')
print(inventory.head(10))

staten_island = inventory.iloc[:10]
print(staten_island)

product_request = staten_island.product_description
print(product_request)

# Finds all seeds in Brooklyn
seed_request = inventory[(inventory.location == 'Brooklyn') & (inventory.product_type == 'seeds')]
print(seed_request)

brooklyn_inven = inventory[inventory.location == 'Brooklyn']
print(brooklyn_inven)

inventory['in_stock'] = inventory.apply(lambda row: True if row.quantity > 0 else False, axis=1)

inventory['total_value'] = inventory.apply(lambda x: (x.quantity * x.price) if x.in_stock is True else 0, axis=1)

combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)
inventory['full_description'] = inventory.apply(combine_lambda,axis=1)
print(inventory)