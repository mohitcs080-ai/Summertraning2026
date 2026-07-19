a=5
print(type(a))
b=5.0
print(type(b))
c=2+4j
print(type(c))

s1='w'
s2="welcom"
s3="""welcome to the geeks world
welcome to the geeks world
welcome to the geeks world"""
print(s1)
print(s2)
print(s3)
name="mohit yadav"
print(name)

a=[]
print(a)

b=["geeks","for","geeks",4,5]
print(b)

Student=["mohit"]
Sub=["maths","eng","science"]
marks=[78,67,89]
print(Student)
print(Sub)
print(marks)

studentrecord=[6567,"mohit","bca",78.67]
print(studentrecord)

l1 =[1,2,[3,4],65]
print(l1)

l2 =["mohit","bca",[78,67,89],90]
print(l2)

count=0
for items in l2:
    if isinstance(items,list):
        for x in items:
            print("\t*  ", x)
        else:
            print(count, items)
            