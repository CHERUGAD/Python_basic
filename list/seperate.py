#Seperation negative and positive numbers
list1=[1,-1,2,-2]
list2=[]
list3=[]
i=0
while i<len(list1):
    if list1[i]<0:
        list2.append(list1[i])
    else:
        list3.append(list1[i])
    i+=1
print(list2,list3)


#Using for loop
list1=[1,-1,2,-2]
list2=[]
list3=[]
for i in list1:
    if list1[i]<0:
        list2.append(list1[i])
    else:
        list3.append(list1[i])
    i+=1
print(list2,list3)


