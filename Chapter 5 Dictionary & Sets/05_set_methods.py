# Creating an empty set
b = set()
print(type(b))

# Adding values to an empty set
b.add(5)
b.add(4)
b.add(4) # Adding a value repeatedly doesnot change a set
b.add((1,4,5))  # Tuples can be added because "tuples" are hashable


# b.add([1,2,3])  # Can not add list in a set because "list" is unhashable
# b.add({4:5})      #Can not add dictionary in a set because "dictionary" is unhashable
print(b)

print(len(b))  # Prints the length of this set 
b.remove(5)
print(b)