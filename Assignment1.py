"""Write a Python program to store marks scored in subject “Fundamental of Data
Structure” by N students in the class. Write functions to compute following:
a) The average score of class
b) Highest score and lowest score of class
c) Count of students who were absent for the test
d) Display mark with highest frequency"""
marks=[95,96,99,45,100,45,91,84,87,99,45,45,78,68,69," "," "," "]
freq={ }
def mainMenu():
    print("These are the marks scored by Students of SE Comp C, in Fundamental of Data Structure\n",marks)
    print("1.   The average score of class: \n")
    print("2.   Highest score and lowest score of class: \n")
    print("3.   Count of students who were absent for the test: \n")
    print("4.   Display mark with highest frequency: \n")
    print("5.   Exit")
    print("\n\n\n")
    ch=int(input("Enter Your Choice: "))

    if (ch==1):
        print(" ")
        avgScore()
        print("=========================================================================================================")
        mainMenu()
    elif (ch==2):
        print(" ")
        highestScore()
        print("=========================================================================================================")
        mainMenu()
    elif (ch==3):
        print(" ")
        absnt()
        mainMenu()
    elif (ch==4):
        print(" ")
        highestFreq()
        print("=========================================================================================================")
        mainMenu()
    elif (ch==5):
        exit()
    else:
        print("Enter valid number!")
        print("=========================================================================================================")
        mainMenu()
def avgScore():
    cnt=0
    avg=0
    total=0
    n=len(marks)
    print("Total strength of SE Comp C class is \n",n)
    for x in marks:
        if type(x)==type(" "):
            cnt=cnt+1
        else:
            total=total+x
    avg=total/(n-cnt)
    print("The average score of the class is \n",avg)
def highestScore():
    max=0
    cnt=0
    for x in marks:
        if type(x)==type(" "):
            cnt=cnt+1
        elif x>max:
            max=x
    print("The Highest marks in FDS Test is \n",max)
    min=0
    Cnt=0
    for x in marks:
        if type(x)==type(" "):
            Cnt=Cnt+1
        elif x<min:
            min=x
    print("The Lowest marks in FDS Test is \n",min)
def absnt():
    absnt=0
    for x in marks:
        if type(x)==type(" "):
            absnt=absnt+1
    print("Count of the students who were absent for FDS Test is \n",absnt)
def highestFreq():
    for i in marks:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    print(freq)

mainMenu()


