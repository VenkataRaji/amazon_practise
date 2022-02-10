"""In a given string replace a set of string with the other"""


# method 1---wihtout using replace

#strings are immutable---so convert the string s1 to list ----why---coz that's the string I need to do the replace
s1=list(map(str,input("Enter the string").split(" ")))
s2=input("Enter string to be replaced with")
s3=input("Enter the substitute string")


if s2 in s1:
    for i in range(len(s1)):
        if s1[i]==s2:
            s1[i]=s3
    print(" ".join(s1))
else:
    print("Not found")

#method 2---usingreplace
s1=input("Enter string for method 2")
s2=input("which string to replace")
s3=input("String to be replaceed with")
s1=s1.replace(s2,s3)
print(s1)
