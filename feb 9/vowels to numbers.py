# replace the vowels with their respective alphabet number

s=input("Enter the string")

for i in s:

    if i=="a" or i=="A":
        s=s.replace(i,"1")
    elif i=="e" or i=="E":
        s=s.replace(i,"5")
    elif i=="i" or i=="I":
        s=s.replace(i,"9")
    elif i=="o" or i=="O":
        s=s.replace(i,"15")
    elif i=="u" or i=="U":
        s=s.replace(i,"21")

print(s)
