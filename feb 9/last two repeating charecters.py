"""For given string print the last two charecters for the length of the input string"""

inp=input("Enter the string")

# it is better to extract the last two 
# char individually and concatenate instaead of string slicing as it comes handy when 
# the len of the inp string is odd.
s=inp[-2]+inp[-1]


iter=len(inp)//2
if len(inp)%2==0:
    print(s*iter)
else:
    print(s * iter+inp[-2]) #concatinating the last second char sepeartely === coz len is odd
