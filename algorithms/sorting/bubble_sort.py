'''this is like comparing two adjacent elements in a list and theis bubles out the biggest number 
to the right most of the list. the algorithm has time complexity of O(n^2) but it has a space complexity of O(1).'''
A = [-5, -9, 1, 5, 6, -5, -7, 10, 2, 3, 8]
def bubbler(lis: list)->list:
    n =len(lis)
    flag =True
    while flag:
        flag =False
        for i in range(1, n):
            if lis[i-1]>lis[i]:
                flag =True
                lis[i-1], lis[i] = lis[i], lis[i-1]
bubbler(A)
print(A)

