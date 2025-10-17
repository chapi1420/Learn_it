'''this is about selecting the minimum out of the list and replacing it to the first element to the list
and iterating this process for the remaining part of the list by excluding the sorted part of the list. time: O(n^2), space O(1)'''


A = [-9, 1, 9, 4, 6, -10, 9, 5, 6, 7, 3, 2, 1, 0]

def selector(lis: list)->list:
    n = len(lis)
    for i in range(n):
        key = lis[i]
        for j in range(i, n):
            if lis[j] < key:
                key = lis[j]
                lis[i], lis[j] = lis[j], lis[i]
selector(A)
print(A)