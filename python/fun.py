#Now I'm working on functions"
def add(a,b):
    total=a+b
    print(total)
add(a=10,b=20)
x=2
y=3
add(x,y)

#for get the sum of number in list
#This is by taking input from user manually
arr=[]
print('Enter tghe number of elemnt add to list')
n=int(input())
for i in range(n):
    num=int(input())
    arr.append(num)
def sum_list(arr):
    total=0
    for i in arr:
        total=total+i
    print(total)
sum_list(arr)


#By using astrix we can call the multiple elements
def sum_list(*a):
    total=0
    for i in a:
        total=total+i
        print(total)
sum_list(10,20,30,40)


#by using return 
def add(a,b):
    
    total=a+b
    return total
sum=add(a=10,b=20)
print( sum)
