# string formatting in python
s = input('Enter your name:')
k = input("Enter your crush's name:")
l = "%s loves %s"%(s,k)
print(l)
a = "{1} loves {0}"
n = a.format(s,k)
print(n)
print(f"Hello:-\n{n}")