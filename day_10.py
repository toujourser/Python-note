### 检查用户输入是否符合参数注解的要求
from functools import wraps
import inspect

def check(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        sig = inspect.signature(fn)
        params = sig.parameters # 有序字典
        # print(params)
        values = list(params.values())
        # flag = True
        for i,p in enumerate(args):
            param = values[i]
            if param.annotation is not param.empty and not isinstance(p,param.annotation):
                print(p,'!==',values[i].annotation)
                # flag = False
                # break
        # if not flag:
        #     raise TypeError('都是你的错')
        for k,v in kwargs.items():
            if params[k].annotation is not inspect._empty and isinstance(v,params[k].annotation):
                print(k,v,'!==',params[k].annotation)
        return fn(*args,**kwargs)
    return wrapper

@check
def add(x:int,y:int=6)->int:
    return x + y

add(20,30)
