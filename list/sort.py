#sorting without sort method and by using for loop and while loop.
list1=[5,1,2,4,3]
n=list1
i=0
while i<len(n)-1:
    j=0
    swapped=False
    while j<len(n)-i-1:
        if n[j]>n[j+1]:
            n[j],n[j+1]=n[j+1],n[j]
            swapped=True
        j+=1
    i+=1
print(n)

#Using for loop to sort the list
list1=[5,2,4,3,1]
n=list1
for i in range(len(n)-1):
    swapped=False
    for j in range(len(n)-i-1):
        if n[j]>n[j+1]:
            n[j],n[j+1]=n[j+1],n[j]
            swapped=True
print(n)