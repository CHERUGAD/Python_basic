#Write a program to find the sum of all elements in a list (without using sum()). 
list1=[1,2,3,4,5]
list2=0
i=0
for i in range(len(list1)):
        list2+=list1[i]
print(list2)


#using while loop
list11 = [1, 2, 3, 4]
list22 = 0
i = 0

while i < len(list11):
    list22 += list11[i]  # Add current element to list2
    i += 1  # Increment index

print(list22)


#Using sum method
list3=[1,2,3,4,5]
print(sum(list3))
