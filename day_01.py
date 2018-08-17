### 给定一个不超过5位的正整数，判断该数的位数，依次打印出 “ 万位、千位、百位、十位、个位 ” 的数字
val = int(input('>>>'))
w = 10000
length = 5
flag = False
while w:
    t = val // w
    if flag:
        print(t)
    else:
        if t:
            print(t)
            flag = True
        else:
            length -= 1
    val %= w
    w //= 10
print(length)


### 给定一个不超过5位的正整数，判断该数的位数，依次打印出 “ 个位、十位、百位、千位、万位 ” 的数字

# No1.
val = int(input('>>>'))
w = 10
length = 5
flag = False
while val:
    t = val % w
    if flag:
        print(t)
    else:
        if t:
            print(t)
            flag =True
        else:
            length -= 1
    val //= w
print(length)



# No2.
val = int(input('>>>'))
w = 10
length = 0
while val:
    print(val%w)
    val //= w
    length += 1
print(length)




### 求100内所有奇数的和（2500）
# No1.
sum = 0
for i in range(1,100,2):
    sum += i
print(sum)


# No2.
sum = 0
for i in range(100):
    if i % 2 != 0:
        sum += i
print(sum)


# No3.
sum = 0
for i in range(100):
    if i & 1:
        sum += i
print(sum)



### 求 1-5 的阶乘之和
t = 1
s = 0
for i in range(1,6):
    t *= i
    s += t
print(t,s)





### 给一个数，判断它是否是素数（质数）

# 质数：一个大于1的自然数只能被1和它本身整除
# 大于3的素数只分布在6n-1和6n+1两数列中。
n = int(input('>>>'))
if n > 3:
    if (n-1) % 6 == 0 or (n+1)%6 == 0:
        print(n,'is primenumber')
else:
    print('No')




### 求10万内的所有素数
# No1.
for i in range(2,100000):
    for j in range(2,int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        print(i,end=' ')
print()


# No2.
lst = [2,3]
for i in range(5,100000,2):
    tmp = i**0.5
    flag = False
    for j in lst:
        if i%j == 0:
            break
        if j > tmp:
            flag = True
            break
    if flag:
        lst.append(i)
print(lst)



# No3.
n = 5
step = 2
while n < 100000:
    for i in range(3,int(n**0.5)+1,2):
        if n % i == 0:
            break
    else:
        print(n,end=' ')

    n += step
    step = 4 if step == 2 else 2



### 打印100以内的斐波那契数列

a = 1
b = 1
print(a,b,end=' ')
while True:
    s = a+b
    if s > 100:
        break
    print(s,end=' ')
    a,b = b,s


### 求斐波那契数列第101项
# No.1
a = 0
b = 1
for i in range(3,103):
    s = a + b
    a,b = b,s
print(s)

# No.2
a = 0
b = 1
c = 2
while True:
    s = a + b
    c += 1
    if c == 101:
        break
    a,b = b,s

print(c,s)


### 输入五个数字，打印每个数字的位数，将这些数字排序打印，要求升序打印
num = 25413
length = len(str(num))
lst = []
while num > 0:
    lst.append(num%10)
    num //= 10
print(lst)

for i in range(length):
    for j in range(length-1-i):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1] = lst[j+1],lst[j]
print(lst)







### 用户输入一个数字
    # 判断是几位数
    # 打印每一位数字及其重复的次数
    # 一次打印每一位数字，顺序个十百千万…位

num = '542452'
length = len(num)
print(length)
lst = [0]*10
for i in num:
    lst[int(i)]+=1

for j in range(10):
    if lst[j]:
        print('{}:{}'.format(j,lst[j]),end=' ')
        
num = int(num)
while num > 0:
    print(num%10,end=',')
    num = num // 10




