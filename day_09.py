### 指定一个源文件，实现copy到目标目录。
    # 例如把 /tmp/test.txt 拷贝到 /tmp/test1.txt

import os
os.chdir('F:\\Python\\code\\mooc')
# print(os.getcwd())

def copy_file(srcfile,destfile):
    with open(srcfile,'r',encoding='utf-8') as src:
        with open(destfile,'w+') as dest:
            for line in src:
                dest.write(line)
copy_file('test.txt','test1.txt')





### 有一个文件，对其进行单词统计，不区分大小写，并显示单词重复最多的10个单词
import os
os.chdir('F:\\Python\\code\\mooc')

def count_word01():
	
	d = {}
	with open('sample.txt',encoding='utf-8') as f:
		
		for line in f:
			line = line.lower()
			n = map(lambda x: x if x.isalnum() else ' ',line)  # 将非字母数字字符转化成空格

			s = ''
			for i in n:
				s += ''.join(i) # 将每行的单个字符拼接为字符串

			str2list = s.split()
			for word in str2list:
				d[word] = d.get(word,0) + 1
	print(sorted(d.items(),key=lambda x:x[1],reverse=True)[:10])

count_word01()



def count_word02():
	def makekey(s:str):
		chars = set(r"""!'"#./\()[],*""")
		key = s.lower()
		ret = []
		start = 0

		for i,c in enumerate(key):
			if c in chars:
				if start == i: # 如果紧挨着还是特殊字符，start一定等于i
					start += 1  #  加1并continue
					continue
				ret.append(key[start:i])
				start = i+1 # 加1是跳过这个不需要的特殊字符c
			else:
				if start < len(key):
					ret.append(key[start:])
		return ret

	d = {}

	with open('sample.txt',encoding='utf-8') as f:
		for line in f:
			words = line.split()
			for wordlist in map(makekey,words):
				for word in wordlist:
					d[word] = d.get(word,0) + 1
	count = 0
	for k,v in sorted(d.items(),key=lambda x:x[1],reverse=True):
		if count > 10:
			break
		print(k,v)
		count +=1

count_word02()







