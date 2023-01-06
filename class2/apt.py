import os,re
import util4file
apt  = util4file.open_csvfile('./class2/apt_201910.csv')
result = []

# search는 찾으면 숫자를 돌려준다.
for i in apt:
    #행 하나를 위한 임시 리스트 생성
    in_list = []
    for j in i:
        try :
            k = i[i.index(j)] = int(re.sub(',','',j))
            in_list.append(k)
        except:
            k = i[i.index(j)]
            in_list.append(k)
            pass
        
        """
        #숫자일경우 전처리 후 추가
        if re.search('\d',j): #정규 표현식 \d : 모든 숫자
            k = int(re.sub(',','',j))
            in_list.append(k)
        
        #문자일경우 그냥 추가
        else:
            in_list.append(j)"""
    result.append(in_list)
print(result)
util4file.wirte_csvfile('./class2/apt_edit.csv',result)