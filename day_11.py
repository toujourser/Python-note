###  实现一个 Cache 装饰器，实现可过期被清除的功能
    # 简化设计，函数的形参定义不包含可变位置参数，可变关键字参数和keyword-only参数
    # 可以不考虑缓存满了之后的换出问题
import datetime
from functools import wraps
import time
import inspect

def mg_cache(duration):
    def _cache(fn):
        local_dict = {} # 对不同函数名是不同的cache

        @wraps(fn)
        def wrapper(*args,**kwargs): # 接受各种参数，kwargs 普通字典的参数无序

            def clear_keys(cache):
                # 清除过期的key
                expire_keys = []
                for k,(_,stamp) in cache.items():
                    now = datetime.datetime.now().timestamp()
                    if now - stamp > duration:
                        expire_keys.append(k)

                for k in expire_keys:
                    cache.pop(k)

            clear_keys(local_dict)

            def make_key():
                # 参数处理，构建key
                sig = inspect.signature(fn) 
                params = sig.parameters # 只读有序的字典
                print(params)
                # print(params['z'].default)

                params_names = [key for key in params.keys()]  # 从params参数字典中获取 key 组成列表
                params_dict = {}  # 用字典来保存参数键值对
                print(params_names)

                for i,v in enumerate(args):  # 遍历获取位置参数作为值，通过参数下标从params_names 中获取形参名作为key
                    k = params_names[i]
                    params_dict[k] = v

                params_dict.update(kwargs) # 将关键字传参添加到params_dict字典中

                # 缺省值处理
                for k,v in params.items(): 
                    if k not in params_dict.keys():
                        params_dict[k] = v.default
                # print(params_dict)

                return tuple(sorted(params_dict)) # 按字典中的key进行排序 解决不同形式的传参方式无法识别为同一种

            key = make_key()

            # 判断是够需要缓存
            if key not in local_dict.keys():
                local_dict[key] = (fn(*args, **kwargs),datetime.datetime.now().timestamp()) # 时间戳

            return local_dict[key][0]
        return wrapper
    return _cache


def logger(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        start = datetime.datetime.now()
        ret = fn(*args,**kwargs)
        delta = (datetime.datetime.now() - start).total_seconds()
        print(fn.__name__, delta)
        return ret
    return wrapper

@logger
@mg_cache(10)
def add(x,y,z=6):
    time.sleep(2)
    return x + y


print(add(9,y=7))
time.sleep(10)
print('************************')
print(add(9,7))
print(add(2,2))
print(d)
print(add(y=1, x=1))
time.sleep(10)
print('***********')
print(add(1,1))
