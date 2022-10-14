def fibbo(n):
    if n<=1:
        return n
    else:
        return (fibbo(n-1)+fibbo(n-2))
a = int(input("Enter a number:"))
print("Fibonacci series is as follows:-\n")
for i in range(a):
    print(fibbo(i))