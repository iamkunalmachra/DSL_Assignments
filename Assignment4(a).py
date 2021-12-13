"""Write a python program to store roll numbers of student in array who attended training program in
random order. Write function for searching whether particular student attended training program or not,
using Linear search and Sentinel search."""
l=[]
def get():
    n=int(input("Enter number of students in class SE: "))
    for i in range(n):
        k=int(input("Enter roll number = "))
        l.append(k)

def dis():
    for i in l:
        print(i,end=" ")

def linear():
    cnt=0
    key=int(input("Enter roll number for searching whether particular"
                  "Student attended training program or not"))
    for i in range(len(l)):
        if (key==l[i]):
            print("Student attended session at ",i," location")
            break
        else:
            cnt+=1
    if(cnt-1==i):
        print("Student did not attend session")

def search():
    i=0
    key=int(input("Enter roll number for searching whether"
                  "particular student attended training program or not "))
    while(i<len(l)):
        if key==l[i]:
            print("Student attended session at ", i, " location")
            break
        i+=1
    if(i==len(l)):
        print("Student did not attend session")

def sentinel():
    item=int(input("Enter roll for searching whether "
                   " Particular student attended training program or not"))
    last=l[-1]
    l[-1]=item
    l=0
    while(item!=l[i]):
        i+=1
    l[-1]=last
    if(i<len(l)-1 or item==l[-1]):
        print("Roll Number is found at ",i," location")
    else:
        print("Roll number is not found")
if __name__== '__main__':
    get()
    dis()

    print("\n1: Linear Search using for Loop")
    print("\n2: Sentinel Search")
    print("\n3: Linear Search using for while")
    ch=int(input("\nEnter choice"))
    if(ch==1):
        linear()

    if(ch==2):
        sentinel()

    if(ch==3):
        search()