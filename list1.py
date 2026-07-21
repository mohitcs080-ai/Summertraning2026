li=[1,2,3,4,4,5,]
print(list[1:4])

print(li[2:])
print(li[-3])
print(li[::3])
print(li[::-3])

l2 = [10,23,45,45,45]
print(l2.remove(45))

print(l2.pop(2))
del l2[1]

print(l2.clear()) 

# INDEXING OF ELEMENT IN LIST 

lst= [10,20,30,40,50,60]
print(lst[0]) # positive indexing
print(lst[-2]) #negative indexing


print("#Slicing in list"*4)
print(lst[:])
print(lst[:3])
print(lst[2:])
print(lst[1:4])
print(lst[-3:])
print(lst[::2])
print(lst[::-1])

print("modifing element"*3)
print
ls= [10,20,30,40]
ls[1]=99
ls[-1]=100
print(ls) 

