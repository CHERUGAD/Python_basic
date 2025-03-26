class person:
    def __init__(self,n,g,a):
         self.name=n
         self.age=a
         self.gender=g
    def talk(self):
         print("Hello, my name is", self.name)
    def vote(self):
         if self.age>=18:
              print("You are eligible to vote")
         else:
              print("You are not eligible to vote")
onj1=person("sam","Male",14)
onj2=person("dom","Female",21)
print(onj1.age,onj2.age)
onj1.talk()
onj1.vote()
onj2.talk()
onj2.vote()