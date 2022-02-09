"""To print the words with the tags given"""

def MakeTags(s1,s2):
    s_Tag="<"+s1+">" #opening tag
    e_Tag ="</"+s1+">"   #closing tag
    print(s_Tag+s2+e_Tag)


# driver code
tag=input("enter the tag")
word=input("enter the word")
MakeTags(tag,word)
