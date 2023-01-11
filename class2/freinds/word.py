#word.py

import os, re, codecs

with codecs.open('./class2/friends/friends101.txt','r','utf-8') as f:
    script101 = f.read()
    line = re.findall(r'\([A-Za-z].+[a-z]|.]\)',script101) # | : or

for i in line:
    print(i)