# 实现ls命令功能,实现-1、-a和-all、 -h选项
#     实现显示路径下的文件列表
#     -a和-all 显示包含.开头的文件
#     -l详细列表显示
#     -h和-l配合,人性化显示文件大小,例如1K、1G、 1T等,可以认为1G=1000M
#     类型字符
#         C字符
#         d目录
#         普通文件
#         l软链接
#         b块设备
#         s socket文件
#         p pipe文件,即FIFO

import argparse
import stat
from pathlib import Path
from datetime import datetime
parser = argparse.ArgumentParser(prog='ls',add_help=True,description='list diretory contents')
parser.add_argument('path',nargs='?',default='.')
parser.add_argument('-a','--all',action='store_true')
parser.add_argument('-l','--list',action='store_true')
parser.add_argument('-hr','--human_readable',action='store_true')

# parser.print_help()
# print(args)

def ls_cmd(path,all=False,detail=False,human=False):

    def _getfiletype(f:path):
        if f.is_dir():
            return 'd'
        elif f.is_block_device():
            return 'b'
        elif f.is_char_device():
            return 'c'
        elif f.is_socket():
            return 's'
        elif f.is_symlink():
            return 'l'
        else:
            return '-'

    modelist = dict(zip(range(9),{'r','w','x','r','w','x','r','w','x'}))
    def _getmodestr(mode:int):
        m = mode & 0o777
        mstr = ''
        for i in range(8,-1,-1):
            if m >> i & 1:
                mstr += modelist[8-i]
            else:
                mstr += '-'

        return mstr

    def _gethuaman(size:int):
        units = 'KMGTP'
        depth = 0
        while size > 1000:
            size = size // 1000
            depth += 1

        return '{}{}'.format(size,units[depth])



    def _listdir(path,all,detail,human):
        p = Path(path)
        for i in p.iterdir():
            if not all and i.name.startswith('.'):
                # print('================')
                continue
            if not detail:
                # print('******************')
                yield (i.name,)
            else:
                st = i.stat()
                # mode = _getfiletype(i) + _getmodestr(st.st_mode)
                mode = stat.filemode(st.st_mode)
                atime = datetime.fromtimestamp(st.st_atime).strftime('%m %d %H:%M:%S')
                size = st.st_size if not human else _gethuaman(st.st_size)
                yield (mode, st.st_nlink, st.st_uid, st.st_gid, size, atime, i.name)

    yield from sorted(_listdir(path,all,detail,human),key=lambda x:x[len(x)-1])

if __name__ == '__main__':
    args = parser.parse_args()
    files = ls_cmd(args.path,args.all,args.list,args.human_readable)
    for i in files:
        print(i)
