from array import *
arr=array('i',[1,2,3,4,5])
print(arr)
print(arr[0])
print(arr[1])
print(arr[2])


from array import *
arr=array('i',[])
x=int(input("Enter the number odf element add to the array"))
print("Enter the %d elemnts in to array"%x)
for i in range(x):
    elements=int(input("Enter the element to be added:"))
    arr.append(elements)
print(arr)


