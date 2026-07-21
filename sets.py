#Set are used to store multiple items in a single variable.
#set items are unchangeable,but you can remove items and add new items.
# sets are written in curley brakets.

sets = {"apple","banana", "chery"}
print(sets)
print(len(sets))

fruit= {"apple","chery"}
fruit.add("orange")
fruit.remove("apple")
print(fruit)

# exercise
ss1={"green","red","blue"}
print(ss1)

ss1.add("yellow")
print(ss1)
ss1.discard("green")
print(ss1)
print(len(ss1))
