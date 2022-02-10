"""Count the number of factors n has excluding 1 and the number itself.

sample test case1:
ip
Enter n10
o/p
2

test case2 :
i/p
Enter n36
o/p
7
"""



n=int(input("Enter n"))

# efficient code.....find the divisors in the range of sqrt(n) and multiply by 2
#why----because all the factors appear as a pair.After sqrt(n) the factors get reversed

ind=int((n**0.5))
c=0
for i in range(2,ind):
    if n%i==0:
        c+=1


if n%ind==0:  #checking if n is a perfect sqaure---if so decrement 1----coz 1 facor would be reapeated twice
    print((c*2)+1)
else:
    print(c*2)

