"""Given a string,generate all (len from 1 to len(s) ) the possible substrings which are consecutive.Consider empty string also

Formula to calculate the number of possible substrings for a given string of len n-----(empty string not counted)

       (n*(n+1))/2"""



"""
test case 1:
i/p
Enter the string  raji

o/p
['r', 'ra', 'a', 'raj', 'aj', 'j', 'raji', 'aji', 'ji', 'i',""]   """



s=input("Enter the string")

ans=[]

j=0

# to generate all the substrings from the len 1 to len(s)
while j!=len(s):
  
# for string slicing
    for i in range(len(s)+1):
        a=s[i:j+1]
        if a!="":
            ans.append(s[i:j+1])
    j+=1
    
# append the empty string also
ans.append("")

print(ans)
