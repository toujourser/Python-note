# Base64编码 ：
import string
alphabet = (string.ascii_uppercase + string.ascii_lowercase + string.digits + '+' + '/').encode()
d = dict(zip(range(64),alphabet))
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
        # print(triple,b)


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

print(base64encode('abc'))


# Base64 解码
import string
base_tbl = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+' + '/'
alphabet = dict(zip(base_tbl,range(64)))

def base64decode(src:bytes):
    ret = bytearray()
    length = len(src)

    step = 4 # 对齐的，从字符到index
    for offset in range(0, length, step):
        tmp = 0x00
        block = src[offset:offset+step]
        for i in range(4):
            index = alphabet.get(block[-i-1])
            if index is not None: # 注意不能是0
                tmp += index << i*6
        ret.append(tmp.to_bytes(3,'big'))
    return bytes(ret.rstrip(b'\x00')) # 把最右边的\x00去掉，不可变

base64decode()