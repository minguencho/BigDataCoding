import pandas as pd
import re

# read_csv() csv file을 dataframe으로 바꿔주는 함수
df = pd.read_csv('./class3/apt.csv',encoding='cp949')
print(df)

# head() : 상단 부분만 선택해서 출력
print(df.head())
# tail() : 하단 부분만 선택해서 출력
print(df.tail())

print(df.지역)
print(df['지역'])

#조건 별로 출력하기
# 조건 확인(T/F)
print(df.면적 > 50)
# 조건에 맞는 정보 추출
print(df[df.면적>130])