import os, csv, codecs, re

# CSVfile 열어서 리스트로 정리 함수
def open_csvfile(filename):
    f = codecs.open(filename,'r','utf-8')
    csvreader  = csv.reader(f)
    output = []
    for i in csvreader:
        output.append(i)

    return(output)

#CSVfile 생성하기
def wirte_csvfile(filename, data):
    f = codecs.open(filename,'w','utf-8')
    csvobject = csv.writer(f,delimiter=',') #delimiter : 구분자
    csvobject.writerows(data)
    f.close()

#쉼표 제외하기
def switch(filename):
    # search는 찾으면 숫자를 돌려준다.
    result = []
    for i in filename:
        #행 하나를 위한 임시 리스트 생성
        in_list = []
        for j in i:
            try :
                #re.sub('pattern','대체,'원본') : 원본에서의 패턴을 대체로 바꿔줌
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
            
            #문자일경우 그냥 추가lsrm
            else:
                in_list.append(j)"""
        result.append(in_list)
    return result