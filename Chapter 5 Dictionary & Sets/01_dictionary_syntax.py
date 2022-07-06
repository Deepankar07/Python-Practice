Dict = {
    "Fast" : "In a quick manner",
    "Depix" : "A sexy guy",
    "Marks" : [1, 2, 3],
    "Anotherdict" :{"Depix" : "a guy"}
}
# print(Dict["Fast"])
# print(Dict["Depix"])
# print(Dict['Marks'])
Dict["Marks"] = [45,25]         # Its mutable
print(Dict['Marks'])
print(Dict['Anotherdict'] ['Depix'])