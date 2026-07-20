numbers=[x for x in range(4)]
print(numbers)

numbers2=[x*x for x in range(4)]
print(numbers2)

even=[x for x in range(10) if x%2==0]
print(even)

odd=[x for x in range(10) if x%2!=0]
print(odd)


words=["lucknow","kanpur","gorakhpur"]
upperword=[words.upper()for words in words]
print(upperword)

lengths=[len(word) for word in words]
print(lengths)

longwords=[len(word) for word in words if len(word)>6]
print(longwords)