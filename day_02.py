### 打印一个边长为n的正方形
# ****
# *  *
# *  *
# ****

# No1.
n = int(input('>>>'))
for i in range(4):
    if i == 0 or i == 3:
        print('*'*n)
    else:
        print('*'+' '*(n-2)+'*')

# No2. 对称
n = int(input('>>>'))
e = -(n//2)
for i in range(e,n+e):
    if i == e or i == n+e-1:
        print('*'*n)
    else:
        print('*'+' '*(n-2)+'*')




### 打印菱形
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

# No1.
n = 7
e = -(n//2)
for i in range(e,n+e):
    print(' '*abs(i) + '*'*(n-2*abs(i)))


# No2.
for i in range(3,-4,-1):
    print(' '*abs(i),end='')
    for j in range(-3,4):
        if abs(i) + abs(j) < 4:
            print('*',end='')
    print()


# No3.
n = 7
e = -(n//2)
for i in range(e,n+e):
    for j in range(1,n+1):
        if abs(i) < j < n-abs(i)+1:
            print('*',end='')
        else:
            print(' ',end='')
    print()




### 空心菱形
#    *
#   * *
#  *   *
# *     *
#  *   *
#   * *
#    *

n = 7
e = -(n//2)
for i in range(e,n+e):
    print(' '*abs(i)+('*' + (' '*(n-2*abs(i)-2) if (n-2*abs(i)) > 1 else '')+('' if (n-2*abs(i)) == 1 else '*')))




### 对顶三角
# *******
#  *****
#   ***
#    *
#   ***
#  *****
# *******

n = 7
e = -(n//2)
for i in range(e,n+e):
    print(' '*(-e-abs(i)) + '*'*(2*abs(i)+1))



### 打印闪电
#    *
#   **
#  ***
# *******
#    ***
#    **
#    *
n = 7
e = -(n//2)
for i in range(e,n+e):
    if i<0:
        print(' '*abs(i) + '*'*abs(-n//2-i))
    elif i>0:
        print(' '*abs(e) + '*'*abs(-n//2+i))
    else:
        print('*'*n)





### 打印九九乘法表
# 1*1=1   
# 1*2=2   2*2=4   
# 1*3=3   2*3=6   3*3=9   
# 1*4=4   2*4=8   3*4=12  4*4=16  
# 1*5=5   2*5=10  3*5=15  4*5=20  5*5=25  
# 1*6=6   2*6=12  3*6=18  4*6=24  5*6=30  6*6=36  
# 1*7=7   2*7=14  3*7=21  4*7=28  5*7=35  6*7=42  7*7=49  
# 1*8=8   2*8=16  3*8=24  4*8=32  5*8=40  6*8=48  7*8=56  8*8=64  
# 1*9=9   2*9=18  3*9=27  4*9=36  5*9=45  6*9=54  7*9=63  8*9=72  9*9=81

for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={}\t'.format(j,i,i*j),end='')
    print()



# 1*1=1   1*2=2   1*3=3   1*4=4   1*5=5   1*6=6   1*7=7   1*8=8   1*9=9   
# 2*2=4   2*3=6   2*4=8   2*5=10  2*6=12  2*7=14  2*8=16  2*9=18  
# 3*3=9   3*4=12  3*5=15  3*6=18  3*7=21  3*8=24  3*9=27  
# 4*4=16  4*5=20  4*6=24  4*7=28  4*8=32  4*9=36  
# 5*5=25  5*6=30  5*7=35  5*8=40  5*9=45  
# 6*6=36  6*7=42  6*8=48  6*9=54  
# 7*7=49  7*8=56  7*9=63  
# 8*8=64  8*9=72  
# 9*9=81  
for i in range(1,10):
    for j in range(i,10):
        print('{}*{}={:<4}'.format(i,j,i*j),end='')
    print()



# 1*1=1   1*2=2   1*3=3   1*4=4   1*5=5   1*6=6   1*7=7   1*8=8   1*9=9   
#         2*2=4   2*3=6   2*4=8   2*5=10  2*6=12  2*7=14  2*8=16  2*9=18  
#                 3*3=9   3*4=12  3*5=15  3*6=18  3*7=21  3*8=24  3*9=27  
#                         4*4=16  4*5=20  4*6=24  4*7=28  4*8=32  4*9=36  
#                                 5*5=25  5*6=30  5*7=35  5*8=40  5*9=45  
#                                         6*6=36  6*7=42  6*8=48  6*9=54  
#                                                 7*7=49  7*8=56  7*9=63  
#                                                         8*8=64  8*9=72  
#                                                                 9*9=81 
for i in range(1,10):
    for j in range(i,10):
        print('{}*{}={:<4}'.format(i,j,i*j),end='')
    print()
    print('{:>8}'.format(' ')*i,end='')



 #                                                               1*1=1  
 #                                                        2*1=2  2*2=4  
 #                                                 3*1=3  3*2=6  3*3=9  
 #                                         4*1=4  4*2=8  4*3=12 4*4=16  
 #                                 5*1=5  5*2=10 5*3=15 5*4=20  5*5=25  
 #                         6*1=6  6*2=12 6*3=18 6*4=24  6*5=30  6*6=36  
 #                 7*1=7  7*2=14 7*3=21 7*4=28  7*5=35  7*6=42  7*7=49  
 #         8*1=8  8*2=16 8*3=24 8*4=32  8*5=40  8*6=48  8*7=56  8*8=64  
 # 9*1=9  9*2=18 9*3=27 9*4=36  9*5=45  9*6=54  9*7=63  9*8=72  9*9=81
for i in range(1,10):
    line = ''
    for j in range(1,i+1):
        line += '{}*{}={:<{}}'.format(i,j,i*j,3 if j<4 else 4)
    print('{:>70}'.format(line))



### 列表解析式实习九九乘法表
# No1.
[[print('{}*{}={}{}'.format(i,j,i*j,'\n' if i == j else ' '),end='')] for i in range(1,10) for j in range(1,i+1) ]

# No2.
[[print('{}*{}={:<3}'.format(i,j,i*j), end='\n' if i == j else '')] for i in range(1,10) for j in range(1,i+1) ]






### 给定一个3*3方阵，求转置矩阵
# 1 2 3       1 4 7
# 4 5 6   =>  2 5 8
# 7 8 9       3 6 9

# No1.
lst = [[1,2,3],[4,5,6],[7,8,9]]
length = len(lst)
for i in range(length):
    for j in range(i):
        lst[i][j],lst[j][i] = lst[j][i],lst[i][j]
print(lst)

# No2.
lst = [[1,2,3],[4,5,6],[7,8,9]]
print(lst)
length = len(lst)
for i in range(length):
    for j in range(length):
        if i < j:
            break
        else:
            lst[i][j],lst[j][i] =  lst[j][i],lst[i][j]
print(lst)




### 给定一个矩阵，求其转置矩阵
# 1 2 3            1 4
# 4 5 6   <==>     2 5
#                  3 6

# No1.   一次性开辟空间
lst = [[1,2,3],[4,5,6]]
print(lst)
length = len(lst)
nlst = [[],[],[]]
for i in range(length+1):
    for j in range(length):
        nlst[i].append(lst[j][i])
print(nlst)

# No1.1
lst = [[1,2,3],[4,5,6]]
length = len(lst)
nlst = [[0 for i in range(length)] for j in range(lst[0])]
for i in range(len(nlst)):
    for j in range(len(nlst[0])):
        nlst[i][j] = lst[j][i]
print(nlst)


# No2.
lst = [[1,2,3],[4,5,6]]
nlst2 = []
for i in zip(lst[0], lst[1]):
    nlst2.append(i)
print(nlst2)

# No2.2
list(zip(lst[0],lst[1]))


# No3.
lst = [[1,2,3],[4,5,6]]
length = len(lst)
nlst = [[],[],[]]
print(lst)
for i in lst:
    for j,col in enumerate(i):
        nlst[j].append(col)
print(nlst)


# No4.
lst = [[1,2,3],[4,5,6]]
length = len(lst)
nlst = [[0 for i in range(length)] for j in range(len(lst[0]))]

for i,row in enumerate(nlst):
    for j,col in enumerate(lst):
        nlst[i][j] = lst[j][i]
print(nlst)