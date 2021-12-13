"""In second year computer engineering class, group A student’s play cricket, group B students play badminton and group C students play football.
Write a Python program using functions to compute following: -

a) List of students who play both cricket and badminton
b) List of students who play either cricket or badminton but not both
c) Number of students who play neither cricket nor badminton
d) Number of students who play cricket and football but not badminton.
(Note- While realizing the group, duplicate entries should be avoided, Do not use SET built-in functions)"""
class_SEA = ["DEVANG", "KUNAL", "ATHARVA", "ANSHU", "SAYYED", "TANISHQ", "JOSHI", "PARTH", "BRIAN", "SAHIL"]
print("Total Students in SE C class are...", class_SEA)

cricket = ["KUNAL", "ANSHU", "TANISHQ", "PARTH" ]
print("Students who play Cricket = ", cricket)

badminton = ["ATHARVA", "SAYYED", "TANISHQ", "PARTH"]
print("Students who play Badminton", badminton)

football = ["DEVANG", "JOSHI"]
print("Students who play Football", football)

# creating empty lists
common = []
only_Cricket = []
only_Badminton = []
Cricket_Badminton = []
play_neither_Cricket_nor_Badminton = []
Cricket_Football = []
Cricket_Football_not_Badminton = []


def mainMenu():
    print(" ")
    print("1. List of common Students who play both Cricket and Badminton")
    print("2. List of Students who play either Cricket or Badminton not both")
    print("3. List of Students who play neither Cricket or Badminton")
    print("4. List of Students who play Cricket and Football but not Badminton")
    print("5. Exit")

    print(" ")
    ch = int(input("Enter Your Choice: "))

    if (ch == 1):
        print(" ")
        play_both_Cricket_and_Badminton()
    elif (ch == 2):
        print(" ")
        either_Cricket_or_Badminton()
    elif (ch == 3):
        print(" ")
        neither_Cricket_nor_Badminton()
    elif (ch == 4):
        print(" ")
        play_Cricket_Football_not_Badminton()
    elif (ch == 5):
        exit()
    else:
        print("Enter Valid Number")


def play_both_Cricket_and_Badminton():
    for i in cricket:
        for j in badminton:
            if i == j:
                common.append(i)
    print("List of common Students who play both Cricket and Badminton are : ", common)


def either_Cricket_or_Badminton():
    for i in cricket:
        flag = 0
        for j in badminton:
            if (i == j):
                flag = 1
        if flag == 0:
            only_Cricket.append(i)
    print("List of Students who play only Cricket are : ", only_Cricket)

    for i in badminton:
        flag = 0
        for j in cricket:
            if (i == j):
                flag = 1
        if (flag == 0):
            only_Badminton.append(i)
    print(" ")
    print("List of Students who play only Badminton are : ", only_Badminton)


def neither_Cricket_nor_Badminton():
    for i in cricket:
        Cricket_Badminton.append(i)
    for j in badminton:
        flag = 0
        for k in Cricket_Badminton:
            if j == k:
                flag = 1
        if flag == 0:
            Cricket_Badminton.append(j)
    print("List of Students who play both Cricket and Badminton are :", Cricket_Badminton)

    for i in class_SEA:
        flag = 0
        for j in Cricket_Badminton:
            if i == j:
                flag = 1
        if flag == 0:
            play_neither_Cricket_nor_Badminton.append(i)
    print(" ")
    print("List of Students who play neither Badminton nor Cricket are : ", play_neither_Cricket_nor_Badminton)


def play_Cricket_Football_not_Badminton():
    for i in cricket:
        Cricket_Football.append(i)
    for j in football:
        flag = 0
        for k in Cricket_Football:
            if j == k:
                flag = 1
        if flag == 0:
            Cricket_Football.append(j)
    print("List of Students who play Cricket and Football ", Cricket_Football)

    for i in Cricket_Football:
        flag = 0
        for j in badminton:
            if j == i:
                flag = 1
        if flag == 0:
            Cricket_Football_not_Badminton.append(i)
    print("")
    print("List of Student who play Cricket and Football but not Badminton", Cricket_Football_not_Badminton)

mainMenu()


