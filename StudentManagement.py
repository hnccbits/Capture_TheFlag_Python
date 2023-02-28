class Student:
    def __init__(self, name, code, branch, bat, age):
        self.name = name
        self.code = code
        self.branch = branch
        self.bat = bat
        self.age = age

max_size = 20

stu = [None] * max_size
tempstu = [None] * max_size
sortstu = [None] * max_size
sortstu1 = [None] * max_size

num = 0

def build():
    global num
    print("Build The Table")
    print(f"Maximum Entries can be {max_size}")

    num = int(input("Enter the number of Entries required: "))

    if num > 20:
        print("Maximum number of Entries are 20")
        num = 20

    print("Enter the following data:")

    for i in range(num):
        name = input("Name: ")
        code = int(input("Student ID: "))
        branch = input("Branch: ")
        bat = int(input("Batch: "))
        age = int(input("Age: "))
        stu[i] = Student(name, code, branch, bat, age)

    show_menu()

def insert():
    global num
    if num < max_size:
        i = num
        num += 1
        code = int(input("Student ID: "))
        for j in range(num):
            if stu[j].code == code:
                print("Duplicate Student Id")
            else:
                name = input("Name: ")
                branch = input("Branch: ")
                bat = int(input("Batch: "))
                age = int(input("Age: "))
                stu[i] = Student(name, code, branch, bat, age)
    else:
        print("Student Table Full")

    show_menu()

def deleteIndex(i):
    for j in range(i, num - 1):
        stu[j].name = stu[j].name
        stu[j].code = stu[j].code
        stu[j].branch = stu[j].branch
        stu[j].bat = stu[j].bat
        stu[j].age = stu[j].age

def deleteRecord():
    code = int(input("Enter the Student ID to Delete Record: "))

    for i in range(num):
        if stu[i].code == code:
            del stu[i]
            num -= 1
            break

    show_menu()

def searchRecord():
    code = int(input("Enter the Student ID to Search Record: "))

    for i in range(num):
        if stu[i].code == code:
            print(f"Name: {stu[i].name}")
            print(f"Student ID: {stu[i].code}")
            print(f"Branch: {stu[i].branch}")
            print(f"Batch: {stu[i].bat}")
            print(f"Age: {stu[i].age}")
            break

    show_menu()

def display():
    print("\tName\tStudent ID\tBranch\tBatch\tAge")
    print("\t  ","_"*60)
    for i in range(num):
        print(f"\t{stu[i].name}\t{stu[i].code}\t\t{stu[i].branch}\t{stu[i].age}\t{stu[i].bat}")
    show_menu()


def updateRecord():
    code = int(input("Enter the Student ID to Search Record: "))
    flag = 0
    for i in range(num):
        if stu[i].code == code:
            flag=1
            stu[i].name = input("Name: ")
            stu[i].branch  = input("Branch: ")
            stu[i].bat = int(input("Batch: "))
            stu[i].age = int(input("Age: "))
            break

    if flag == 0:
        print("Invalid Student ID")

    show_menu()

def show_menu():
    print("\n\n-------------------------")
    print("Capture The Flag")
    print("-------------------------\n")

    print("Available Options:\n")
    print("Build Table         (1)")
    print("Insert New Entry    (2)")
    print("Delete Entry        (3)")
    print("Search a Record     (4)")
    print("Display Record      (5)")
    print("Update Record       (6)")
    print("Exit                (7)")
    option = int(input())
    if (option == 1):
        build()
    elif (option == 2):
        insert()
    elif (option == 3):
        deleteRecord()
    elif (option == 4):
        searchRecord()
    elif (option == 5):
        display()
    elif (option == 5):
        updateRecord()
    elif (option == 7):
        sys.exit("Program exited")
    else:
        print("Expected Options are 1/2/3/4/5/6/7")
        show_menu()
show_menu()
