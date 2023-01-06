# prac_popSeoul.py

# csv file을 불러 올 떼 셀 안의 숫자가 ''에 감싸져 와서
# 숫자가 아닌 문자로 인식된다.
# 이 문제를 해결하기 위해서 ''를 제거하고 숫자형으로 바꿔준다. 
# 또한 숫자가 세자리마다 ,로 구분되기 때문에 ,도 제거한다.

#module
import os, re, util4file

total = util4file.open_csvfile('./class2/popSeoul.csv')

#re.sub('pattern','대체,'원본') : 원본에서의 패턴을 대체로 바꿔줌

result = []

# search는 찾으면 숫자를 돌려준다.
for i in total:
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

#파일에 작성
util4file.wirte_csvfile('./class2/popSeoul_edit.csv',result)