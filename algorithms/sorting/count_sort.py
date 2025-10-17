A = [-9, 1, 9, 4, 6, -10, 9, 5, 6, 7, 3, 2, 1, 0]

def count_sort(lis: list) -> list:
    maxx = max(lis)
    minn = min(lis)
    _range = maxx - minn + 1  
    
    shifted = [x - minn for x in lis]
    
    counts = [0] * _range
    for num in shifted:
        counts[num] += 1

    sorted_list = []
    for i in range(_range):
        sorted_list.extend([i + minn] * counts[i])  

    return sorted_list

A = count_sort(A)
print(A)
