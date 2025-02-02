"""Find the intersection between two list"""
list_1=[1,3,5,7,8]
list_2=[1,2,3,4,5,6,7,8]
new_list=[]
i=0
while i<len(list_1):
    for element in list_2:
        if list_1[i]==element:
            new_list.append(list_1[i])
            break
    i+=1
print(new_list)

#Using for loop
list3=[1,2,3,4,5]
list4=[2,5,6,7]
new=[]
for i in list3:
    for j in list4:
        if i==j:
            new.append(i)
print(new)