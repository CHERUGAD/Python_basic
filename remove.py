"""remove duplicates from original"""
new_list=[1,2,3,4,5,64,3]
remove_ele=3
new_list.remove(remove_ele)
print(new_list)  # Output: [1, 2, 4, 5,64,3]
#this code is for single element removal

"""By using loops to find repeating element in the list"""
new_list=[1,2,3,4,5,64,3]
i=0
remove_elem=3
nw_list=[]
while i<len(new_list):
    if new_list[i]!=remove_elem:
        nw_list.append(new_list[i])
    i+=1
print(nw_list)
