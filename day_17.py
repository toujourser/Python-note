import re
### 匹配邮箱地址 ###
email = '''test@hot-mail.com
    v-ipp@magedu.com
    web.manager@magedu.com.cn
    supper.user@google.com
    a@w-a-com'''

def email_re(email:str):
    #regex = re.compile('(?:\w+[.-]*\w*@\w+[-]*\w+\.[a-z]+[.]*[a-z]*)')
    regex = re.compile('([\w-.]+@[\w-.]+\.\w+)')
    result = regex.findall(email)
    print(result)

# email_re(email)




### 匹配HTML标记内的内容 ###

html = "<a href='http://www.magedu.com/index.html' target='_blank'>马哥教育</a>"
def html_re(html:str):
    regex = re.compile('(?<=\>).*(?=\<.*>)')
    result = regex.search(html)
    print(result.group())

# html_re(html)



### 匹配URL ###

url = """http://www.magedu.com/index.html
https://login.magedu.com
file:///ect/sysconfig/network
"""
def url_re(url:str):
    regex = re.compile('[a-z]*:/{2,3}\w+.*')
    result = regex.findall(url)
    print(result)

# url_re(url)




### 匹配二代中国身份证ID ###

id_card = """321105700101003
321105197001010030
11210020170181054X
"""

def id_re(id_card:str):
    regex = re.compile('(\d{6}[12]\d{3}[01](?:(?:(?!<1)[3-9])|[0-2])[0-3](?:(?:(?!<3)[2-9])|[0-9])\d{3}[\dX])|^(\d{6}\d{2}[01](?:(?:(?!<1)[3-9])|[0-2])[0-3](?:(?:(?!<3)[2-9])|[0-9])\d{3})(?!\d)')
    # |(\d{6}\d{2}[01][0-2][0-3]\d{3})
    result = regex.findall(id_card)
    print(result)

# id_re(id_card)




### 判断密码强弱 ###

psd = """atWb32_67mnq"""
def pwd_re(psd:str):
    key = {'a-z','A-Z','_','\d'}
    for i in key:
        i = '['+i+']'
        regex = re.compile(i)
        if not regex.search(psd):
            print('bad')
            break
    else:
        print('good')
# pwd_re(psd)






### 单词统计 wordcount ###

def topn(srcfile,n=10,ignore=None):
    def makekey(line:str,chars=set('''!'"#@^~%&./\:;| ()‘[],+*-—???\r\n''')):
        start = 0
        for i,c in enumerate(line):
            if c in chars:
                if start == i: # 如果紧挨着还是特殊字符，start一定等于i
                    start += 1 # 加1并continue
                    continue
                yield line[start:i]
                start = i+1 # 加1是跳过这个不需要的特殊字符c
        else:
            if start < len(line):
                yield line[start:]

    regex = re.compile('[^\w]+')
    def makekey2(line: str):
        for i in regex.split(line):
            if len(i):
                yield i
    dk = {}
    def word_count():
        key_set = set()
        dk = {}
        with open(srcfile,encoding='utf-8') as f:
            for line in f:
                for word in map(str.lower,makekey2(line)):
                    if word not in ignore:
                        dk[word] = dk.get(word,0) + 1
        return sorted(dk.items(),key=lambda x:x[1],reverse=True)[:n]

    return word_count()

print(topn('sample.txt',ignore={'the','is','a','and','if','of','to'}))

