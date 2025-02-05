# Cumulative Sum Write a program to compute the cumulative sum of a list (e.g., [1, 2, 3] → [1, 3, 6]). 
# The function should return a new list and not modify the original list.
list1=[1,2,3]
list2=[]
sum=0
for i in list1:
    sum+=i
    list2.append(sum)
print(list2)