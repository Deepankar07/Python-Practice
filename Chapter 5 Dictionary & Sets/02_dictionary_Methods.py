dict = {
    "fast" : "In a quick manner",
    "depix" : "A sexy guy",
    "marks" : [1, 2, 3],
    "anotherdict" :{"Depix" : "a guy"},
    1 : 2
}

# Dictionary Methods
print(dict.keys())
print(type(dict.keys()))
print(list(dict.keys()))   #print the keys of dictionary   # type casting in list
print(dict.values())
print(dict.items())  # print (key, values) of all contents of dictionary

updatedict = {
    "lovish" : "friend",
    "depix" : "writer"
}
dict.update(updatedict) # updates the dictionary by adding key-value pairs from updatedict
print(dict)

print(dict.get("depix"))
print(dict.get("depix2"))   # Returns none as depix2 is not present in the dictionary
# print(dict["depix2"])      # throws an error as depix2 is not present in the dictionary