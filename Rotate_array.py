s=input("Enter string to be reversed: ")
def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]
  
s = "Hacktoberfestshreek"
  
print ("The original string  is : ",end="")
print (s)
  
print ("The reversed string(using recursion) is : ",end="")
print (reverse(s))
