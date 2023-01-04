# actor.py
# 등장인물 정리

# module
import os, re, codecs

# 정규 표현식에 맞춰 actor 이름 추출
with codecs.open('friends101.txt','r','utf-8') as f:
    script101 = f.read()
    # : 를 만나기 전까지 A-Z or a-z 가 반복(+)된다.
    char = re.compile(r'[A-Z][a-z]+:')
    # 집합 자료형 처리는 중복을 지원하지않는다. 
    # list -> set -> list   
    line = list(set(re.findall(char,script101)))

# actor가 아닌 사람 제외 하기
for one_line in line:
    if one_line == 'Note:' or one_line == 'Scene:' or one_line == 'All:' :
        pass
    else : 
        print(one_line[:-1])

