'''this is another advanced algorithm that uses the concept of recurstion to sort elements in an array.
it divides a list into the left side, right side and middle number to be useed as comparison.
in this case, we will be taling the last element as the middle comparison base and the left side is the set of list less 
than the middle index, whi(le the right side contains those greater than the base'''

A = [-9, 1, 9, 4, 6, -10, 9, 5, 6, 7, 3, 2, 1, 0]

def quick_sort(lis: list)-> list:
    if len(lis)<=1:
        return lis
    p = lis[-1]
    L = [x for x in lis[:-1] if x <=p]
    R = [x for x in lis[:-1] if x >p]

    L =quick_sort(L)
    R =quick_sort(R)

    return L + [p] + R
b =quick_sort(A)
print(b)