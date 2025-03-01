from statistics import mean as m 
admins={"cherugad":'12345678'}
std_dict= {'jeff' : [78,45,65],
            'ravi':[56,89,65] }





def entergrades():
    nametoenter=input("Student Name")
    gradetoenter=float(input("Enter grade"))
    if nametoenter in std_dict:
        print("Adding Grade...")
        std_dict[nametoenter].append(gradetoenter)
    else:
        print("Student does not exist")
    print(std_dict)
def removeStudent():
    nameToremove=input("Enter the name to remove :")
    if nameToremove in std_dict:
        print("Removing student")
        del std_dict[nameToremove]
    print(std_dict)
def findAvg():
    for eachStudent in std_dict:
        gradeList=std_dict[eachStudent]
        avrGrade=m(gradeList)
        print(eachStudent,"Has an average of",avrGrade)
def main():
    print("Welcome to Grade Central")

    while True:
        print("[1]-ENter Grades\n")
        print("[2]-Remove Stuednt\n")
        print("[3]-Student Average Grades\n")
        print("[4]-Exit\n")
        choice=int(input("What would you like to do today ? (Enter a number)"))
        if choice==1:
            entergrades()
        elif choice==2:
            removeStudent()
        elif choice == 3:
            findAvg()
        elif choice == 4 :
            exit()
        else :
            print("Invalid option selected") 

login=input("Username")
password=(input("Password"))
if login in admins:
    if admins[login]==password:
        print("Welcome",login)
        while True:
            main()
    else:
        print("Inavalid username")
else:
    print("Inalid password <enter again>")