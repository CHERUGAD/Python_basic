n=int(input("Enter the number"))
nr=0
while n>0:
    rem=n%10 #123%10=3 gives remainder or last digit
    nr=nr*10+rem #0*10+3=3 gives reverse number

    n=n//10 #123//10=12 gives quotient or remaining number or removing last digit
print(nr)


n=int(input("Enter the number"))
nr=0
revr=int(str(n)[::-1])
print(revr)