t1=()
print(t1)
t2=tuple()
print(t2)
t3=(10,22,23,0)
print(t3)
print(t3[2])
print(type(t3))

t4=("bca",34,54, True)
print(t4[-2])

# slicing in tuples
# tuples[start:stop:step]
t5=(10,20,30,40,50,60,30,60,30)
print(t5)
print("#"*10)
print(t5[::2]) # ending exclusive

#count
#index


print(t5.count(30))
print(t5.index(30))
print(len(t5))
print(max(t5))
print(min(t5))
print(sum(t5))
print(sorted(t5))
print(20 in t5)
print(20 not in t5)
