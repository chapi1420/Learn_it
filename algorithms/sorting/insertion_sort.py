'''thi is one of the simplest sorting algorithms. you will have two indextes playing this role 
and you idealy split the list into sorted and unsorted region. It has time complexity of O(n^2) nad space comlexity of O(1)'''

A = [-9, 1, 9, 4, 6, -10, 9, 5, 6, 7, 3, 2, 1, 0]
def insert_srt(lis: list)->list:
    n = len(lis)
    for i in range(1, n):
        key = lis[i]
        j = i-1
        while j>=0 and lis[j]>key:
            lis[j+1] = lis[j]
            j -=1
        lis[j+1] =key
    return lis
insert_srt(A)
print(A) 
