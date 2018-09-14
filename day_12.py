### 写一个命令分发器
    # 程序员可以方便的注册函数到某一个命令，用户输入命令时，路由到注册的函数
    # 如果此命令没有对应的注册函数，执行默认函数
    # 用户输入用 input('>>>')
from functools import partial
def commend_dispatcher():
    cmd_tbl = {} # 构建全局字典
    def reg(cmd, *args, **kwargs):
        def _reg(fn):
            newfn = partial(fn, *args, **kwargs)
            cmd_tbl[cmd] = newfn
            return newfn
        return _reg

    # 缺省函数
    def defaultfn():
        print('Unknown command')


    # 调度器
    def dispatcher():
        while True:
            cmd = input('>>> ')
            if cmd.strip() == '': # 退出条件
                return
            cmd_tbl.get(cmd,defaultfn)()

    return reg, dispatcher

reg,dispatcher = commend_dispatcher()

# 自定义函数
@reg('py',x=2)
def foo1(x=3):
    print('python',x)

@reg('mag')
def foo2():
    print('mage')

# 调度循环
dispatcher()