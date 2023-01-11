# prac_popSeoul.py

# csv file을 불러 올 떼 셀 안의 숫자가 ''에 감싸져 와서
# 숫자가 아닌 문자로 인식된다.
# 이 문제를 해결하기 위해서 ''를 제거하고 숫자형으로 바꿔준다. 
# 또한 숫자가 세자리마다 ,로 구분되기 때문에 ,도 제거한다.

#module
import os, re, util4file

total = util4file.open_csvfile('./class2/popseoul/popSeoul.csv')
newPop = util4file.switch(total)

"""i = newPop[1]

for i in newPop:
    foreign = 0
    try :
        #round(값, n) : n의 자리까지 반올림
        foreign = round(i[2]/(i[1]+i[2])*100,1)
        print(i[0],foreign)
    except :
        pass
print('-----end-----')"""

#외국인 비율이 3(3.0)% 넘을 때만 출력하기

"""for i in newPop:
    foreign = 0
    try :
        #round(값, n) : n의 자리까지 반올림
        foreign = round(i[2]/(i[1]+i[2])*100,1)
        if foreign >= 3.0 :
            print(i[0],foreign)
    except :
        pass
print('-----end-----')
"""
#컬럼 추가
new = [['구','한국인','외국인','외국인 비율']]

for i in newPop:
    foreign = 0
    try :
        #round(값, n) : n의 자리까지 반올림
        foreign = round(i[2]/(i[1]+i[2])*100,1)
        new.append([i[0],i[1],i[2],foreign])
    except :
        pass

util4file.wirte_csvfile('./class2/popseoul/newPop.csv', new)