import os, csv, codecs

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