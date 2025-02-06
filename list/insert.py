#Insert an element into a list at a given position using insert(). 
list2=[1,2,3,4]
list2.insert(0,5)
print(list2)


list3=[1,2,3,4]
i=0
while i<len(list3):
    list3.insert(i,5)
    i+=2
print(list3)

list4=[1,2,3,4]
#Insert an element into a list at a given position using insert().
for i in range(0,len(list4),3):
    list4.insert(i,5)
print(list4)
