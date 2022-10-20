n=int(input(“Enter size of array\n“))
arr=list(map(int,input(“Enter elements of array\n“).split()))
arr.sort(reverse=False) #arr.sort() also be used
print(“Ascending order array”)
print(*arr)
arr.sort(reverse=True)
print(“Descending order array”)
print(*arr)
