'''Rearrange a list so that even numbers come first, followed by odd numbers, while maintaining their relative order.'''
element=[1, 2, 3, 2, 4, 2, 5]
even_numbers=[]
odd_numbers=[]
for number in element:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)
new_list=even_numbers+odd_numbers
print(new_list)

###Using while loop
elementt=[1, 2, 3, 2, 4, 2, 5]
even_numbers=[]
odd_numbers=[]
i=0
while i<len(elementt):
    if elementt[i]%2==0:
        even_numbers.append(elementt[i])
    else:
        odd_numbers.append(elementt[i])
    i+=1
new_listt=even_numbers+odd_numbers
print(new_listt)