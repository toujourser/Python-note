# 打印一棵树
import math

origin = [30,20,80,40,50,10,60,70,90]

# 居中方案对齐
def print_tree01(array, unit_width=2):
    length = len(array)
    depth = math.ceil(math.log2(length+1))  # 获取 深度
    width = 2**depth-1  # 获取最大宽度，
    index = 0

    for i in range(depth): # 0 - 4
        for j in range(2**i): #
            # 居中后打印，后面追加一个空格
            print('{:^{}}'.format(origin[index],width*unit_width),end=' '*unit_width)
            index += 1
            if index >= length:
                break
        width //= 2 # 居中打印宽度减半
        print() # 控制换行

# print_tree01(origin)


origin2 = [0,30,20,80,40,50,10,60,70,90] # 最前面补0
# 投影栅格实现
def print_tree02(array,unit_width=2):
    length = len(array)
    index = 1
    depth = math.ceil(math.log2(length)) # 因为前面补0了，不然应该是math.ceil(math.log2l(len(array)+1))
    # print(depth)

    sep = ' '*unit_width
    for i in range(depth-1,-1,-1):
        pre = 2 ** i - 1
        print(sep*pre,end='') # 前置空格
        offset = 2 ** (depth - i - 1) # 计算上一行数字对本行宽度的影响
        line = array[index:index+offset] # 取数字
        # print(line)
        intervalspace = sep*(2*pre+1) # 元素之间的空格
        print(intervalspace.join(map(str,line))) # join 数据
        index += offset



print_tree02(origin2)


if __name__ == '__main__':
    print_tree02(origin2)