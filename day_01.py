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

# 方法一：
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



# 方法二：
val = int(input('>>>'))
w = 10
length = 0
while val:
    print(val%w)
    val //= w
    length += 1
print(length)




