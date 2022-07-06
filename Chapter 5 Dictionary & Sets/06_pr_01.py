mydict = {
    "pankha" : "Fan",
    "dabba"  : "Box",
    "vastu"  : "Item"
}
print("options are", mydict.keys())
a= input("Enter the hindi word\n")
# print("the meaning of your word is:", mydict[a])


# Below line will not throw error if a key is  not present in the dictionary because .get is used
print("the meaning of your word is:", mydict.get(a))