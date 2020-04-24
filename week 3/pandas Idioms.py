'''
Suppose we are working on a DataFrame that holds information on our equipment for an upcoming backpacking trip.

Can you use method chaining to modify the DataFrame df in one statement to drop any entries where 'Quantity' is 0 and rename the column 'Weight' to 'Weight (oz.)'?

'''

print(df.head())

# Your code here

print(df.drop(df[df['Quantity'] == 0].index).rename(columns={'Weight': 'Weight (oz.)'}))