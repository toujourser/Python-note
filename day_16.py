# 堆排序
import math
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

origin = [0,30,20,80,40,50,10,60,70,90] # 为了和编码对应，增加一个无用的0在首位
print_tree02(origin)
print('=='*30)

total = len(origin)-1 # 初始待排序元素个数，即n 长度去掉0


def heap_adjust(n,i,array:list):
    """
    调整当前节点（核心算法）
    调整的结点的起点在n//2，保证所有调整的结点都有孩子结点
    :param n: 待比较数个数
    :param i: 当前节点的下标
    :param array: 待排序数据
    """
    while 2*i <= n:
        lchild_index = 2*i
        max_child_index = lchild_index
        if n > lchild_index and array[lchild_index+1]>array[lchild_index]:
            max_child_index = lchild_index + 1

        if array[max_child_index] > array[i]:
            array[i],array[max_child_index] = array[max_child_index],array[i]
            i = max_child_index

        else:
            break

# heap_adjust(total,total//2,origin)
# print(origin)
# print()
# print_tree02(origin)

def max_heap(total,array):
    for i in range(total//2,0,-1):
        heap_adjust(total,i,array)
        # print('* '*30)
        # print_tree02(array)
    return array
# max_heap(total,origin)
print_tree02(max_heap(total,origin))
print('**'*30)


def sort(total,array:list):
    while total > 1:
        array[1],array[total] = array[total],array[1]
        total -= 1
        if total == 2 and array[total] >= array[total-1]:
            break

        heap_adjust(total,1,array)
    return array
print(sort(total,origin))

