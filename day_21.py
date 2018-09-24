# 将前面的链表，封装成容器
# 要求：
# 1、提供__getitem__、__iter__、__setitem__方法
# 2、使用一个列表，辅助完成上面的方法
# 3、进阶：不使用列表，完成上面的方法
# 本例未采用list，使用链表完成插入、删除，但是查询效率低


class Node:  # 节点保存内容和前后节点信息
    def __init__(self, item, next=None, prev=None):
        self.item = item
        self.next = next
        self.prev = prev

    def __repr__(self):
        return "({} <= {} => {})".format(
            self.prev.item if self.prev else None,
            self.item,
            self.next.item if self.next else None)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.__size = 0

    def __len__(self):
        return self.__size


    def append(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node  # 设置开头结点，以后不变
        else:
            self.tail.next = node  # 当前最后一个结点关联下一个跳
            node.prev = self.tail  # 前后关联
        self.tail = node  # 更新结尾结点

        self.__size += 1
        return self

    def iternodes(self, reverse=False):
        current = self.head if not reverse else self.tail
        while current:
            yield current
            current = current.next if not reverse else current.prev

    def insert(self, index, item):
        if index < 0:  # 不接受负数
            raise IndexError('Not negative index {}'.format(index))

        current = None
        for i, node in enumerate(self.iternodes()):
            if i == index:
                current = node
                break
        else:
            self.append(item)
            return

        node = Node(item)  # 待加入的结点
        prev = current.prev  # 前一个
        next = current  # 后一个

        if prev is None:  # 头部 i==0
            self.head = node
        else:  # 不是首元素
            node.prev = prev
            prev.next = node
        node.next = next
        next.prev = node
        self.__size += 1

    def pop(self):  # 尾部移除
        if self.tail is None:  # 空
            raise Exception('Empty')

        node = self.tail
        item = node.item
        prev = node.prev

        if prev is None:  # only one node
            self.head = None
            self.tail = None
        else:
            prev.next = None
            self.tail = prev

        self.__size -= 1
        return item

    def remove(self, index):
        if self.tail is None:  # 空
            raise Exception('Empty')

        if index < 0:
            raise IndexError('Not negative index {}'.format(index))

        current = None
        for i, node in enumerate(self.iternodes()):
            if i == index:
                current = node
                break
        else:  # not found
            raise IndexError('Wrong index {}'.format(index))

        prev = current.prev
        next = current.next

        # 4种情况
        if prev is None and next is None:
            self.head = None
            self.tail = None
        elif prev is None:  # 头部
            self.head = next
            next.prev = None
        elif next is None:
            self.tail = prev
            prev.next = None
        else:
            prev.next = next
            next.prev = prev

        del current
        self.__size -= 1

    def __getitem__(self, index):
        reverse = True if index < 0 else False
        start = 1 if index < 0 else 0
        for i,node in enumerate(self.iternodes(reverse),start):
            if i == abs(index):
                return node
            else:
                raise IndexError

    def __setitem__(self, index, value):
        self[index].item = value

    __iter__ = iternodes


l = LinkedList()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
l.remove(0)
l.pop()
l.insert(2, 5)
print(len(l))
l[0] = 'f'
for i in l.iternodes():
    print(i)
