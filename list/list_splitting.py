'''5.	Split a list into n nearly equal parts.'''
List_1=[1,2,3,4,5,6,7,8,9]
new1=[]
new2=[]
new3=[]
n=3
i=0
while i<len(List_1):
    if i<n:
        new1.append(List_1[i])
    elif i>=n and i<2*n:
        new2.append(List_1[i])
    else:
        new3.append(List_1[i])
    i+=1
print(f"{new1}\n{new2}\n{new3}")

