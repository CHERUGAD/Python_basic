 #Find the largest and smallest numbers in a list using loops (without max() or  min()). 
list1=[1,2,3,4,5,6,7]
largest = list1[0]
smallest=list1[0]
for item in list1:
    if item > largest:
        largest = item
    elif item < smallest:
        smallest = item
print(f"Largest element is {largest} and the smallest element in the list is{smallest}")

#Using While loop
list1=[1,2,3,4,5,6,7]
largest = list1[0]
smallest=list1[0]
i=0
while i<len(list1):
    if list1[i] > largest:
        largest = list1[i]
    elif list1[i] < smallest:
        smallest = list1[i]
    i+=1
print(f"Largest element is {largest} and the smallest element in the list is{smallest}")

#By using min and max mehtod()
list1=[1,2,3,4,5,6,7]
print(f"Largest element is {max(list1)} and the smallest element in the list is{min(list1)}")

