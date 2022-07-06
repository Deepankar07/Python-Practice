# similar to "f" string
name="Deepankar"
channel="CNN"
type="news"

#a="This is {} and his {} channel is {}.".format(name,type,channel)
a="This is {1} and his {0} channel is {2}.".format(name,type,channel)   # can type it according to their indices

print(a)