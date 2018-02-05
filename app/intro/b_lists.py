'''
You’ve already seen Python strings, which are sequences of characters. 

Python has two other sequence structures: tuples and lists. These contain zero or more elements. 
Unlike strings, the elements can be of different types.

Why does Python contain both lists and tuples? 

Tuples are immutable; when you assign elements to a tuple, they’re baked in the cake and can’t be changed. 
Lists are mutable, meaning you can insert and delete elements with great enthusiasm.

Run Script from project root dir:
  python -m app.intro.b_lists or in this dir as python b_lists.py


'''

ne_sales_engineers = ['mondeux', 'colin', ' fernando', ' john', ' kaz', 'Anthony']
type(ne_sales_engineers)

ne_sales_engineers.append('Fernando')
ne_sales_engineers


list('deep security')

# Combine lists by using extend() or +=
east_sales_engineers = ['westphal', 'chris', 'kenJo', 'Vitaliy', 'Geoff', 'colin']
ne_sales_engineers += east_sales_engineers
ne_sales_engineers


#access elements of List
ne_sales_engineers[1]
ne_sales_engineers[:3]
ne_sales_engineers[-1:]

ne_sales_engineers.remove('Vitaliy')
ne_sales_engineers.pop()

# list comprehension
c_names = [x for x in ne_sales_engineers if x.startswith('c')]



# Dictionaries -> key, value store

pocs = {'casey': 12, 'colin': 20, 'geoff': 3, 'chris': 0}
print(pocs['casey'])
pocs['chris'] = 5

import json
print(json.dumps(pocs))

for key, value in pocs.items():
    print("{}:{}".format(key, value))


print('geoff' in pocs.keys())
