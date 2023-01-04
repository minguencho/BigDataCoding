# friends.py
# friends 대본 정리 프로그램

# import module
import os
import re
import codecs

# 대본 파일 불러와서 Monica 대사 추출하기
with codecs.open('friends101.txt','r','utf-8') as f:
    script101 = f.read()
    line = re.findall(r'Monica:.+',script101)
    #print(line[:3])
    """i = 0
    for one_line in line:
        print(one_line)
        i = i + 1
    print(i)"""

# monica 저장된 것을 copy파일에 쓰기
with codecs.open('friends101 copy.txt','w','utf-8') as f:
    monica = ''
    for one_line in line:
        #monica = monica + one_line
        monica += one_line
    f.write(monica) #write에서 \n이 살아 있기 때문에 자동 줄바꿈됨

#copy 파일 읽기
with codecs.open('friends101 copy.txt','r','utf-8') as f:
    print(f.read())
