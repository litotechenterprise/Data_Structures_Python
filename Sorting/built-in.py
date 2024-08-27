
# Python's sort() method sorts items in place
[1, 50, 10000, 510, 5050, 60].sort() # [1, 50, 60, 510, 5050, 10000]

# Pass in a keyword argument to sort in descending order
[1, 50, 10000, 510, 5050, 60].sort(reverse = True) # [10000, 5050, 510, 60, 50, 1]

# Strings sort as expected
['March', 'Jan', 'Feb', 'Dec'].sort() # ["Dec", "Feb", "Jan", "March"]

# Use a lambda function to sort by object property
[{ "score": 20 }, { "score": 100 }, { "score": 5 }].sort(key = lambda x: x["score"])
# => [{ "score": 5 }, { "score": 20 }, { "score": 100 }]