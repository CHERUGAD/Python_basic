##Write a program to remove all occurrences of a specific element from a list.
element=[1, 2, 3, 2, 4, 2, 5]
element.remove(2)  #for removing specific one element 
print(element)

##By using loops
original_list = [1, 2, 3, 2, 4, 2, 5]
element_to_remove = 2
filtered_list = []
for item in original_list:
    if item != element_to_remove:
        filtered_list.append(item)
    
print(filtered_list)

##Using while loops"""

original_list = [1, 2, 3, 2, 4, 2, 5]
elemen_to_remove = 2
filtered_list = []
while elemen_to_remove in original_list:
    original_list.remove(elemen_to_remove)
print(original_list)

