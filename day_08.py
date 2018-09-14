# 求2字符串的最长公共子串
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

