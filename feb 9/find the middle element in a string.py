# # find the middle charecter of the string given the str(len) is always odd

s=input("Enter the input") 
ind=len(s)//2  #the index does not take float value

# the string index always starts from 0---> so no need to add +1
print(s[ind])
