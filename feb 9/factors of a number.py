"""find the number of factors for a given number"""

n=int(input("Enter n"))
c=0

# original logic----To iterate from 1 to n (1,n) 
for i in range(1,n+1):
    if n%i==0:
        c+=1
print(c)

# method 2---->sqrt() method
"""logic---->the factors always appear in pairs 
for eg for 16----(1,16),(2,8),(4,4),(8,2),(16,1)----these are the possible combinations 
     so this boils downs that the factors of 16 are 1,2,4,8,16----so 5
                 observation ----after a certain number,the o/p just becomes reverse...
                 just find the max point number after which the factors reverses
                 the max limit is the sqrt(n)---coz,both the factors would be same"""
                
ind=int(n**0.5)
for i in range(1,ind+1):   #I am just iterating the for loop till sqrt(n) not till n---so the iteration reduces from n to sqrt(n)
#     if n%i==0:      #checking if the given number is divisble
        c+=1
if n%(n**0.5)==0:      #if the inp number is a perfect square then the same number is repated twice,so just subtarct 1 from the count
    print("count is",(c*2)-1)
else:
    print("count is",c*2)
