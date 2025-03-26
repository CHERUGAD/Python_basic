import random
nump=random.randint(100,1000)
print("Guess the number between 10 and 100",nump)
guess=int(input())
n=0
digit=0
while guess!=10:
    if guess%10==0:
        digit=guess%10
        n=n*10+digit
        guess=guess//10
        if guess==nump:
          print("Congratulations, you have guessed the number")
        
    else:
        print("Try again, the number is matched")
    break