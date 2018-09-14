#### 将配置ini 文件 ,转换成json格式
# [DEFAULT]
# a = test
#
# [mysql]
# default-character-set = utf8
# a = 1000
#
# [mysqld]
# datadir = /dbserver/data
# port = 33060
# character-set-server=utf8
# sql_mode=NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES

import os
import json
from configparser import ConfigParser
os.chdir('F:/Python/code/mooc')
srcfile = 'test.ini'
destfile = 'test.json'

def ini2json(src,dest):
    cfg = ConfigParser()
    cfg.read(src)
    d = {}
    for k,v in cfg.items():
        d[k] = dict(cfg.items(k))

    with open(dest,'w') as f:
        json.dump(d,f)
    print(d)

ini2json(srcfile,destfile)