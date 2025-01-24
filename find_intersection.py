"""Find the intersection between two list"""
list_1=[1,3,5,7,8]
list_2=[1,2,3,4,5,6,7,8]
new_list=[]
i=0
while i<len(list_1):
    for list1 in list_2:
        if list1==list_1[i]:
            new_list.append(list1)
i+=1
print(new_list)