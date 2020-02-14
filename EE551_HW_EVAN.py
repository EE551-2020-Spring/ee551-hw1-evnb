#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# %load EE551_HW1.py
#!/usr/bin/python

"""
Python Core object Types
"""

# In[1]:

import math

# In[5]:

def numbers_and_strings():
    """
    This is to review numbers and strings and basic operations.
    """
    # Assign a string "EE551" to a variable x
    x = "EE551"

    # Assign a string "Stevens" to a variable y
    y = "Stevens"

    # Repeat variable y 5 times
    z = y*5

    # What is the length of z?
    length = len(z)

    # Concatenate variable y with string " is good"
    m = y + " is good"

    # Replace "good" with "awesome" in variable m and assign it to a new variable n
    n = m.replace("good", "awesome")

    return x, y, z, length, m, n

def lists():
    """
    This is to review basic operations with lists.
    """
    n = "Stevens is awesome"

    # Split variable n on a delimiter space into a list of substrings
    nlist = n.split()

    # Get all the items past the first of the third substring
    someitems = nlist[2][1:]

    # Create a 3 x 3 matrix as nested list such that
    #   first row is [1, 4, 5]
    #   second row is [6, 10, 11]
    #   third row is [12, 17, 38]
    matrix = [[1, 4, 5], [6, 10, 11], [12, 17, 38]]

    # Collect the items in the last column of matrix A using list comprehension
    lastcolumn = [row[-1] for row in matrix]

    # Collect only the even items of the diagonal of matrix A using list comprehension
    diagonalevens = [matrix[i][i] for i in range(len(matrix)) if matrix[i][i]%2==0]

    # We can convert a single character to its underlying integer code (e.g., its ASCII byte value)
    # by passing it to the built-in ord function. Generate a list of these integers to represent
    # each character of the string "Stevens" using list comprehension.
    asciilist = [ord(c) for c in "Stevens"]

    return nlist, someitems, lastcolumn, diagonalevens, asciilist

def dictionaries():
    """
    This is to review basic operations with dictionaries.
    """
    # Create a dictionary that maps:
    #   fruit => "apple"
    #   quantity => 4
    #   color => "green"
    dictionary = {"fruit" : "apple", "quantity" : 4, "color" : "green"}

    # Get the item in dictionary f that the key "fruit" maps to
    fruitval = dictionary["fruit"]

    # Increase the quantity of f by 1
    # IMPLEMENT IT HERE
    ++ dictionary["quantity"]

    # Create a nested dictionary where:
    #   name => {first_name => "Grace", last_name => "Hopper"} (a dictionary)
    #   jobs => ["scientist", "engineer"] (a list)
    #   age => 85
    nesteddictionary = {"name" : {"first_name" : "Grace", "last_name" : "Hopper"}, "jobs" : ["scientist", "engineer"], "age" : 85}

    # Add "programmer" to the list of jobs Grace has
    # IMPLEMENT IT HERE
    nesteddictionary["jobs"] += ["programmer"]

    # Get the third job Grace has that you recently added
    thirdjob = nesteddictionary["jobs"][2]

    # Use the sort() function to get sorted keys of amazing_grace in alphabetically ascending order
    gracekeys = list(nesteddictionary)

    gracekeys.sort()

    return a, f, p, k

numbers_and_strings()
lists()
dictionaries()