### 冒泡排序
# No1. 升序

lst = [1,9,8,5,6,7,4,2,3,-2]
length = len(lst)
for i in range(length):
    for j in range(length-1-i):
        if lst[j] > lst[j+1]:
            lst[j],lst[j+1] = lst[j+1],lst[j]
print(lst)


# No2. 优化
lst = [1,9,8,5,6,7,4,2,3,-2]
length = len(lst)
for i in range(length):
    flag = False
    for j in range(length-1-i):
        if lst[j] > lst[j+1]:
            lst[j],lst[j+1] = lst[j+1],lst[j]
            flag = True
    if not flag:
        break
print(lst)




### 简单选择排序
# No.1
lst = [1,9,8,5,6,7,4,2,3,-2]
length = len(lst)
for i in range(length):
    maxindex = i
    for j in range(i+1,length):
        if lst[j] > lst[maxindex]:
            maxindex = j
    if i != maxindex:
        lst[i],lst[maxindex] = lst[maxindex],lst[i]
print(lst)


# No2. 降序
lst = [1,9,8,5,6,7,4,2,3,-2]
length = len(lst)
for i in range(length):
    minindex = i
    for j in range(i+1,length):
        if lst[j] < lst[minindex]:
            minindex = j
    if i != minindex:
        lst[i],lst[minindex] = lst[minindex],lst[i]
print(lst)


# No3. 优化

lst = [1,9,8,5,6,7,4,2,3,-2]
length = len(lst)

for i in range(length//2):
    maxindex = i
    minindex = -i-1
    minorigin = minindex
    for j in range(i+1,length-i):
        if lst[j] > lst[maxindex]:
            maxindex = j
        if lst[-j-1] < lst[minindex]:
            minindex = -j-1
    if lst[maxindex] == lst[minindex]:
        break
    if i != maxindex:
        lst[i],lst[maxindex] = lst[maxindex],lst[i]
        if i == minindex or i == length + minindex:
            minindex = maxindex
    if minorigin != minindex and lst[minindex] != lst[minorigin]:
        lst[minorigin],lst[minindex] = lst[minindex],lst[minorigin]
print(lst)

