"""Write a program to reverse a list without using reverse() or slicing."""
list1=[9,7,6,54,3,2]
list2=[]
i=0
while i<len(list1):
    list2.append(list1[-(i + 1)])
    i+=1
print(list2)

#By using for loop will reverse a list
list3 = [9, 8, 7, 6]
list4 = []

# Iterate over indices from the end of the list to the start
for i in range(len(list3)):
    list4.append(list3[-(i + 1)])  # Correct negative indexing
print(list4)
