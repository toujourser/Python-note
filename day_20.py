origin = [37, 99, 73, 48, 47, 40, 40, 25, 99, 51]
newlist = sorted(origin)


def insert_sort(lst, i):
    low = 0
    high = len(lst)
    while low < high:
        mid = (low + high) // 2
        if lst[mid] < i:
            low = mid + 1
        else:
            high = mid
    lst.insert(low, i)


# for i in (40, 20, 41, 100):
#     insert_sort(newlist, i)
# print(newlist)


import bisect


def get_grade(score):
    breakpoints = [60, 70, 80, 90]
    grades = 'EDCBA'
    return grades[bisect.bisect(breakpoints, score)]


for x in (91, 82, 77, 65, 50, 60, 70):
    print('{}->{}'.format(x, get_grade(x)))
