import time
import re
import random
import datetime
import threading
import matplotlib.pyplot as plt
from queue import Queue
from pathlib import Path
from pandas import Series
from user_agents import parse
import macpath
from functools import update_wrapper

filepath = Path('E:/我的坚果云/Python/slides/py12/chapter07/logs/test.log')
# filepath = Path('E:/我的坚果云/Python/slides/py12/chapter07/logs')


ops = {'datetime':lambda timer:datetime.datetime.strptime(timer,'%d/%b/%Y:%H:%M:%S %z'),
       'status':int,
       'length':int,
       'useragent':lambda ua:parse(ua),
       }
patter = '''(?P<remote>[\d.]{7,15}) - - \[(?P<datetime>[/\w +:]+)\] "(?P<method>\w+) (?P<url>\S+) (?P<protocol>[\w/\d.]+)" (?P<status>\d+) (?P<length>\d+) .+ "(?P<useragent>.+)"'''

regex = re.compile(patter)

def extract(line:str)->dict:
    result = regex.match(line)
    if result:
        return {name:ops.get(name,lambda x:x)(data) for name,data in result.groupdict().items()}



def loadfile(path:str,encoding='utf-8'):
    with open(path,encoding=encoding) as f:
        for line in f:
            fileds = extract(line)
            if isinstance(fileds,(dict,)):
                yield fileds
            else:
                continue


# 加载目录
def load(*paths,ext='*.log',encoding='utf-8',r=False):
    for path in paths:
        p = Path(path)
        if p.is_dir():
            if isinstance(ext,str):
                ext = [ext]
            else:
                ext = list(ext)

            for e in ext:
                files = p.rglob(e) if r else p.glob(e)
                for file in files:
                    yield from loadfile(str(file.absolute()),encoding=encoding)

        else:
            yield from loadfile(str(p.absolute()),encoding=encoding)



def window(src:Queue,handle,width,interval):
    """
    窗口函数
    :param src: 数据源，缓存队列 ，用来获取数据
    :param handle:  数据处理函数
    :param width:  时间窗口宽度，秒
    :param interval: 处理时间间隔，秒
    """
    start = datetime.datetime.strptime('19700101 00:00:00 +0800', '%Y%m%d %H:%M:%S %z')
    curret = datetime.datetime.strptime('19700101 00:00:00 +0800', '%Y%m%d %H:%M:%S %z')
    buf = [] # 窗口中待计算数据
    delta = datetime.timedelta(seconds=width - interval)

    while True:
        # data = next(iteable)
        # 从队列中获取数据
        data = src.get()
        if data:
            buf.append(data) # 存入临时缓冲等待计算
            curret = data['datetime']

        # print(curret,start)
        # 每隔interval计算buf中的数据一次
        if (curret - start).total_seconds() > interval:
            print('*'*30)
            # print(threading.current_thread())
            ret = handle(buf)
            print('{}'.format(ret))
            start = curret

            # 清除超出width的数据
            buf = [x for x in buf if x['datetime'] > curret - delta]


# 数据处理函数
def handle(iterable):
    return iterable

# 状态码占比分析
def status_handle(iterable):
    # 统计时间窗口内的一批数据
    status = {}
    for item in iterable:
        key = item['status']
        status[key] = status.get(key,0) + 1
    # print(status)
    total = len(iterable)
    return {k:status[k]/total for k,v in status.items()}

browser_total = {}
def browser_handle(iterable):
    browser={}
    for b in iterable:
        ua = b['useragent']
        key = ua.browser.family,ua.browser.version_string
        browser[key] = browser.get(key,0) + 1
        browser_total[key] = browser_total.get(key,0) + 1
    # print('$$$$$$$$$$',sorted(browser_total.items(), key=lambda items: items[1], reverse=True)[:10])
    return browser



# 分发器
def dispatcher(src):
    # 分发器中记录hangdler，同时保存各自的队列
    handles = []
    queues = []


    def reg(handle,width,interval):
        """
        注册 窗口处理函数
        :param handle: 注册的数据处理函数
        :param width: 时间窗口宽度
        :param interval: 时间间隔
        """
        q = Queue()
        queues.append(q)

        t = threading.Thread(target=window,args=(q,handle,width,interval))
        handles.append(t)


    def run():
        for h in handles:
            h.start()  # 启动进程

        while True:
            for item in src:
                for q in queues:
                    q.put(item) # 将数据源中取到的数据分发到所有队列中
            while True:
                cmd = input('<<<')
                if cmd == 'plot':
                    # print(sorted(browser_total.items(), key=lambda items: items[1], reverse=True)[:10])
                    newdict = {}
                    for (k,v),val in browser_total.items():
                        newdict[k] = newdict.get(k,0) + val
                    print(sorted(newdict.items(), key=lambda items: items[1], reverse=True)[:10])


                    s = Series(newdict)
                    # s = s.sort_values(ascending=False)
                    print(s)
                    # s.plot()
                    # plt.plot(s)
                    # plt.Circle(s)
                    s.plot.pie()
                    plt.show()


    return reg,run

if __name__ == '__main__':
    reg,run = dispatcher(load(filepath))
    # reg(handle,10,5)
    # reg(status_handle,10,5)
    reg(browser_handle,10,10)
    run()

