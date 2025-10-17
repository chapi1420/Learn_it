'''merge sort uses the idea ou recursion to split the list into subsequent parts and then it 
meres the sorted lists. This is advanced sorting algorithm and it takes time complexity of O(nlog n)
and space complexity of O(n). the space complexity could be reduced but it would be much complicated 
to do so.'''

A = [-9, 1, 9, 4, 6, -10, 9, 5, 6, 7, 3, 2, 1, 0]
def merge_sort(lis: list)->list:
    if len(lis)==1:
        return lis
    n =len(lis)
    m = n//2
    L = lis[:m]
    R = lis[m:]

    L =merge_sort(L)
    R =merge_sort(R)
    l, r =0, 0
    L_len =len(L)
    R_len =len(R)
    sorted_lis =[0]*n
    i =0

    while l <L_len and r <R_len:
        if L[l]< R[r]:
            sorted_lis[i] = L[l]
            l +=1
        else:
            sorted_lis[i] = R[r]
            r +=1
        i +=1
    while l <L_len:
        sorted_lis[i] =L[l]
        l +=1
        i +=1
    while r <R_len:
        sorted_lis[i] =R[r]
        r +=1
        i +=1
    return sorted_lis

B =merge_sort(A)
print(B)