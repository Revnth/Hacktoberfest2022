#Input the values into the list 
arr = list(map(int, input().split(" "))
           
def part(arr, low, high):
           i = arr[low]
           return i+1
def algso(arr, low, high):
           p = part(arr, low, high)
           algso(arr, p+1, high)
           algso(arr, low, p-1)
           
           
algso(arr, 0, len(arr) - 1)
           
