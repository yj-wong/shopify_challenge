import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset1 = pd.read_csv("dataset1.csv")

print('We plot the order amount as historgam and scatter plot to examine the data.\n')
# Plot the graph as histogram
order_amount = dataset1['order_amount'].copy()
order_amount.sort_values()
plt.hist(np.log10(order_amount), bins=50, figure=plt.figure(figsize=(10, 8)), log=True)
plt.xlabel('Order amount log10')
plt.ylabel('Frequency')
plt.show()

# Plot the graph as scatter plot
plt.plot(dataset1['order_id'], np.log10(dataset1['order_amount']), 'o', figure=plt.figure(figsize=(10, 8)))
plt.xlabel('Order ID')
plt.ylabel('Order amount log10')
plt.show()

# Use median because dataset is skewed
print('As the dataset is shown to be heavily skewed, using median for AOV is better than using mean.')
print('Median order amount for entire dataset is', dataset1['order_amount'].median())
print('Median total items for entire dataset is', dataset1['total_items'].median())
print()

# We split orders into regular, large, and very large from what we see on the plot
print('For futher information, we can see that the order amount can roughly be split into 3 types: regular, large, and very large.')
regular_orders = dataset1[dataset1['order_amount']<=10**3.5]
print('Median order amount for regular orders is', regular_orders['order_amount'].median())
print('Median total items for regular orders is', regular_orders['total_items'].median())
print('The regular orders represent most of the orders, which consist of a one or a few pairs of sneakers that cost several hundred dollars.\n')

large_orders = dataset1[(dataset1['order_amount']>=10**3.5) & (dataset1['order_amount']<=10**5.5)]
print('Median order amount for large orders is', large_orders['order_amount'].median())
print('Median total items for large orders is',large_orders['total_items'].median())
print('The large orders represent the sales of expensive sneakers, which consist of a one or a few pairs of sneakers that cost tens of thousands of dollars.\n')

very_large_orders = dataset1[dataset1['order_amount']>10**5.5]
print('Median order amount for very large orders', very_large_orders['order_amount'].median())
print('Median total items for very large orders',very_large_orders['total_items'].median())
print('we can further examine that this type of very large orders is a regular bulk order from the same store by the same user.')
pd.set_option('display.max_columns', None)
print(very_large_orders.head())
