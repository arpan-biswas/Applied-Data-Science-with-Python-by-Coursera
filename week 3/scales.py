#scales

# Try casting this series to categorical with the ordering Low < Medium < High.

s = pd.Series(['Low', 'Low', 'High', 'Medium', 'Low', 'High', 'Low'])

# Your code here

s.astype('category', categories=['Low', 'Medium', 'High'], ordered=True)
