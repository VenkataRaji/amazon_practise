# AP
"""Given three integers a,d and n ,generate the AP in a single line """

def Ap(start,diff,n):
    print(start,end=",")
    while(n>1):
        start+=diff
        print(start,end=",")
        n-=1

# deiver code
n1=int(input("Enter start value"))
n2=int(input("Enter the diff value"))
n3=int(input("Enter the num of iterations"))

Ap(n1,n2,n3)
