def merge_sort(list):
    '''
    Sorts a given list in ascending order 
    Returns a new sorted list 

    Divide: finds the midpoint of a list and divides it into sublists 
    COnquer: Recursvely sort the sublists created in previous step 
    Combine: Merge the sorted sublists created in previous steps

    Run time = O(n log n)
    '''
    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(list):
    '''
    Divide the unsorted list at midpoint into sub lists 
    Returns two sublists left and right
    '''

    midpoint = len(list) // 2
    left = list[:midpoint]
    right = list[midpoint:]
    return left, right


def merge(left, right):
    '''
    Merges two lists (arrays), sorting them in the process 
    Returns a new merged list

    Runs in  O(n) time
    '''
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l


def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True

    return list[0] < list[1] and verify_sorted(list[1:])


# testing out the code
alist = [23, 56, 7, 8, 9, 34, 54, 67, 4, 24, 6, 89, 65]
l = merge_sort(alist)
print(l)
print(verify_sorted(alist))
print(verify_sorted(l))
