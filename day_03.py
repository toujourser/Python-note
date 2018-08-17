### 简单选择排序
lst = [1,9,4,6,3,8,6,2,7,5]
length = len(lst)
for i in range(length):
    maxindex = i
    for j in range(i+1,length):
        if lst[j] > lst[maxindex]:
            maxindex = j
    if i != maxindex:
        lst[i],lst[maxindex] = lst[maxindex],lst[i]
print(lst)



### 计算杨辉三角前6行
    # 第n行有n项，n是正整数
    # 第n行数字之和为2^(n-1)
    # 只要求打印出杨辉三角的数字即可

# No1. 补零 放在单个列表
n = 6
pre = [1]
for i in range(n):
    pre.append(0)
    nlst = []
    for j in range(i+1):
        nlst.append(pre[j-1]+pre[j])
    pre = nlst
    print(nlst)

# No2. 前后追加 1
lst = [[1],[1,1]]
n = 6
for i in range(2,n):
    nlst = [1]
    pre = lst[i-1]
    for j in range(i-1):
        nlst.append(pre[j]+pre[j+1])
    nlst.append(1)
    lst.append(nlst)
print(lst)


# No3. 折半
triangle = []
n = 6
for i in range(n):
    row = [1]*(i+1)
    triangle.append(row)
    for j in range(1,i//2+1):
        val = triangle[i-1][j-1] + triangle[i-1][j]
        row[j] = val
        if i!= 2*j:
            row[-j-1] = val
print(triangle)


# No4. 单个列表实现
n = 6
row = [1]*n
for i in range(n):
    offset = n - i
    z = 1
    for j in range(1,i//2+1):
        val = z + row[j]
        z = row[j]
        row[j] = val
        if i != 2*j:
            row[-j-offset] = val
    print(row[:i+1])





### 求杨辉三角的第m行第k个元素
    # 第m行有m项，m是正整数，因此k一定不会大于m
    # 第n行的m个数可表示为C(n-1,m-1)，即为从n-1个不同的元素中去m-1个元素的组合数
    # (n-1)!/(m-1)!(n-m)!

# No1.
a=b=c=1
if m > n or n <= 0 or m <= 0:
    print('exit')

for i in range(1,n):
    if i <= n-1:
        a *= i
    if i <= m-1:
        b *= i
    if i <= n-m:
        c *= i
val = a//(b*c)
print(val)


# No2.
m = 9
k = 5
n = m - 1
r = k - 1
d = n - r
targets = []
factorial = 1
for i in range(1,n+1):
    factorial *= i
    if i == r:
        targets.append(factorial)
    if i == d:
        targets.append(factorial)
    if i == n:
        targets.append(factorial)
print(targets[2]//(targets[0]*targets[1]))


# No3.
triangle = []
for i in range(n):
    row = [1]
    triangle.append(row)
    if i == 0:
        continue
    for j in range(1,i):
        row.append(triangle[i-1][j-1]+triangle[i-1][j])
    row.append(1)
# print(triangle)
print(triangle[n-1][m-1])


# No4.
m = 9
k = 5
oldline = []

for i in range(m):
    newline = [1] * (i + 1)
    for j in range(2,i+1):
        newline[j-1] = oldline[j-2] + oldline[j-1]
    oldline = newline
    print(newline)
print(newline[k-1])







### 随机产生10个数字
 ## 要求
    # 每个数字的取值范围[1,20]
    # 统计重复的数字有几个？分别是什么？
    # 统计不重复的数字有几个，分别是什么？
    # 举例：11,7,5,11,6,7,4，其中2个数字7和11重复了，3个数字4、5、6没有重复过
# No1.
nums = [11,7,5,11,6,7,4,11]
length = len(nums)
status = [0]*length
samenums = []
diffnums = []
for i in range(length):
    if status[i] != 0 :
        continue
    count = 0
    for j in range(i+1,length):
        if status[j] != 0:
            continue
        if nums[i] == nums[j]:
            count += 1
            status[j] = count 
    if count:
        count += 1
        status[i] = count
        samenums.append((nums[i],count))
    else:
        diffnums.append(nums[i])
print(samenums,diffnums)




# No2.
nums = [11,7,5,11,6,7,4,11,2,8]
length = len(nums)
lst = [0] * 21
for i in range(10):
    lst[nums[i]] += 1

for j in range(20):
    if lst[j]:
        print('{}:{}'.format(j,lst[j]))





### 字典练习
 ## 用户输入一个数字
  # 打印每一位数字及其重复的次数


from collections import defaultdict
import random

# No1.
num = input('>>>').strip().lstrip('0')
d = {}
for i in num:
    d[i] = d.get(i,0)+1
print(d)

# No2.
num = input('>>>')
d = defaultdict(int)
for i in num:
      d[i] += 1
print(d)

# No3.
num = input('>>>')
d = {}
for i in num:
    if i not in d:
        d[i] = 0
    d[i] += 1
print(d)

# No4.
num = input('>>>')
d = {}
for i in num:
    d[i] = d.setdefault(i, 0) + 1
print(d)







### 数字重复统计
    # 随机产生100个整数
    # 数字的范围[-1000,1000]
    # 升序输出这些数字并打印其重复的次数
# No1.
lst = []
for i in range(100):
    lst.append(random.randint(-1000, 1000))
print(lst)

d = {}
for j in lst:
    d[j] = d.get(j,0) + 1

print(sorted(d.items()))

# No2.
lst = []
for i in range(100):
    lst.append(random.randint(-1000, 1000))
lst.sort()
print(lst)


# No3.
d = defaultdict()
for j in lst:
    d[j] = d.get(j,0) + 1
print(d)



### 字符串重复统计
    # 字符表‘abcdefghijklmnopqrstuvwxyz’
    # 随机挑选2个字母组成的字符串，共挑选100个
    # 降序输出所有不同的字符串及重复的次数

str1 = ''
lst = []
d = {}

for i in range(97,123):
    str1 += chr(i)

# No1.
# sample()
# for i in range(100):
#     s = ''.join(random.sample(str1, 2))
#     lst.append(s)

# No2.
# choice()
for i in range(100):
    for j in range(2):
        lst.append(random.choice(str1)+random.choice(str1))
print(lst)
print('~'*30)

for j in lst:
    d[j] = d.get(j,0) + 1
    # if j not in d:
    #     d[j] = 0
    # d[j] += 1

print(sorted(d.items(),reverse=True))




### "0001.'adgadfgdfs'" 是ID格式，要求ID格式是以点号分割，左边是4位从1开始的整数，右边是
  # 10位随机小写因为字母。请以此生成前100个ID的列表

import string,random
['{:0>4}.{}'.format(i,''.join(random.sample(string.ascii_lowercase, 10))) for i in range(1,100)]
['{:0>4}.{}'.format(i,"".join(random.choices(string.ascii_lowercase,k=10))) for i in range(1,100)]


