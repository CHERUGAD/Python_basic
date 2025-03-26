from threading import *
def show():
    print("This is the child thread")
t=Thread(target=show)
t.start()
print("This is the parent class")


#Using thread in class
from threading import *
class mythread(Thread):     #inherits the properties of main calss 
    def run(self):
        for i in range(5):
            print("This is the child thread",end="\n")
t=mythread()
t.start()
for i in range(5):
    print("This is the parent class")

from threading import *
class ourthread():
    def run(self):
        for i in range(5):
            print("This is the child thread",end="\n")
obj=ourthread()
t=Thread(target=obj.run)
t.start()
for i in range(5):
    print("This is the parent class")
    