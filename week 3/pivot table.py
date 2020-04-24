#pivot table

'''
Suppose we have a DataFrame with price and ratings for different bikes, broken down by manufacturer and type of bicycle.

Create a pivot table that shows the mean price and mean rating for every 'Manufacturer' / 'Bike Type' combination.
'''

print(Bikes)

# Your code here

print(pd.pivot_table(Bikes, index=['Manufacturer','Bike Type']))