### 递归
# 把一个字典扁平化
	# 源字典 {'a':{'b':1,'c':2},'d':{'e':3,'f':{'g':4}}}
	# 目标字典 {'a.b':1,'a,c':2,'d.e':3,'d.f.g':4}




### 递归实现
# 1/
d = {'a':{'b':1,'c':2},'d':{'e':3,'f':{'g':4}}}
target = {}

def dict_demo01(d,key=''):
    for k,v in d.items():
        if isinstance(v,dict):
            dict_demo02(v,key=key+k+'.')
        else:
            target[key+k] = v
    return target



# print(dict_demo01(d))	

# 2/
def dict_demo02(src,dest=None,prefix=''):
    if dest is None:
        dest = {}
    for k,v in src.items():
        if isinstance(v,dict):
            dict_demo03(v,dest,prefix=prefix+k+'.')
        else:
            dest[prefix+k] = v
    return dest


# print(dict_demo02(d))


# for循环
d = {'a':{'b':1,'c':2},'d':{'e':3,'f':{'g':4}}}

def dict_demo03(d):
    target = {}
    for k1,v1 in d.items():
        # print(k1,v1)
        if isinstance(v1,dict):
            for k2,v2 in v1.items():
                # print(k2,v2)
                if isinstance(v2,dict):
                    for k3,v3 in v2.items():
                        # print(k3,v3)
                        target[k1+'.'+k2+'.'+k3] = v3

                else:
                    target[k1+'.'+k2] = v2
    return target

# print(dict_demo03(d))


#### 实现Base64编码

import string
alphabet = (string.ascii_uppercase + string.ascii_lowercase + string.digits + '+' + '/').encode()
d = dict(zip(range(64),chrs))
# print(alphabet,len(alphabet))


def base64encode(src:str):
    ret = bytearray()
    if isinstance(src,str):
        _src = src.encode()
    else:
        return

    length = len(_src)

    # r记录补0 的个数
    r = 0
    for offset in range(0,length,3):
        triple = _src[offset:offset+3] # 切片可以越界
        if offset + 3 > length:
            r = 3-len(triple)
            triple += b'\x00'*r # 便于计算补零

        # 将3个字节看成一个整体转成字节bytes，大端模式
        b = int.from_bytes(triple,'big')


        for i in range(18,-1,-6):
            if i == 18:
                index = b >> i
            else:
                index = b >> i & 0x3F # 0b11 1111
            ret.append(alphabet[index])

    # 替换等号
    if r:
        ret[-r:] = b'='*r # 从索引-r 到末尾使用右边的多个元素依次替换
    return bytes(ret)


# print(base64encode('mds-'))


### 求2字符串的最长公共子串

def findit01(str1,str2):
    length1 = len(str1) 
    length2 = len(str2)
    matrix = [[0]*length1 for i in range(length2)]

    xmax = 0
    xindex = 0

    for i,x in enumerate(str2):
        for j,y in enumerate(str1):
            if x != y: # 两字符不相等
                pass
            else: # 两字符相等
                if i == 0 or j == 0: # 在边上
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = matrix[i-1][j-1] + 1

                # 记录最大值
                if matrix[i][j] > xmax:
                    xmax = matrix[i][j] # 记录最大值，用于下次比较
                    xindex = j

    start = xindex + 1 - xmax
    end = xindex + 1
    # print(matrix,xmax,xindex,start,end)
    return str1[start:end]

print(findit01(s1,s2))



def findit02(str1,str2):
    if len(str1) > len(str2):

        srt1,str2 = str2,str1
    length = len(str1)

    for sublen in range(length,0,-1):
        for start in range(0,length-sublen+1):
            substr = str1[start:start+sublen] # 切割子串
            if str2.find(substr) > -1:
                return substr
print(findit02(s1,s2))


