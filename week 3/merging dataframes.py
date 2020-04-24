#merging dataframes

''' Here are two DataFrames, products and invoices. The product DataFrame has an identifier and a sticker price. The invoices DataFrame lists the people, product identifiers, and quantity. Assuming that we want to generate totals, how do we join these two DataFrames together so that we have one which lists all of the information we need?

products DataFrame:
	Price	Product
Product ID		
4109	5.0	Sushi Roll
1412	0.5	Egg
8931	1.5	Bagel

invoices DataFrame:
	Customer	Product ID	Quantity
0	Ali	4109	1
1	Eric	1412	12
2	Ande	8931	6
3	Sam	4109	2

'''

# products and invoices are already initalized.

print(pd.merge(products, invoices, left_index=True, right_on='Product ID'))
