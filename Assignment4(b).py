"""Write a python program to store roll numbers of student array who attended training program in sorted
order. Write function for searching whether particular student attended training program or not, using
Binary search and Fibonacci search"""
def min(x,y):
    if(x<y):
        return x
    else:
        return y

def fibSearch(arr,x,n):
    f2=0
    f1=1
    fibM=f2+f1   #fibM=1
    while(fibM<n):  #n=11  1<11 yes....|13<11 no
        f2=f1   #1 1 2 3 5
        f1= fibM    #1 2 3 5 8
        fibM=f2+f1  #2 3 5 8 13
    offset = -1  #offset = -1
    while(fibM>1):  #13>1 | 8>1|3>1|2>1
        i=min(offset + f2, n-1) #-1+5=4,1-so i=4|7,10|5,10|6,10
        if(arr[i]<x):   #arr[4]<80ie45<80y|82<80N|50<80y|80<80N
            fibM=f1  #8  |2
            f1=f2
            f2=fibM-f1
            offset=i

        elif(arr[i]>x):
            fibM=f2     #3
            f1=f1-f2
            f2=fibM-f1

        else:
            return i

    if(f1 and arr[offset + 1] == x):
        return offset + 1
    return -1

print("Fibbonacci Search Method: ",end="\n")
arr=[10,22,35,40,45,50,80,82,85,90,100]
print("The element inside arr are as follows: ",end="\n")
print(arr)
n=len(arr)
print("Total elements present in arr are: ",n)
x=int(input("Enter the roll number you want to search in arr:: "))
print(arr)
print(x)
print("Roll number found at index:: ",fibSearch(arr,x,n))