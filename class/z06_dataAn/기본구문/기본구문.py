import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')
df

# 컬럼별 호출
df['키']
df['이름']
df[['이름', '키']]
df[['키','이름']][1:4]
df[df.columns[[1,3,4,]]][1:4]
# 컬럼만 가져오기 
df.columns
df.columns[0:3]
df.columns[[1,4,6]]
                    # <== 위치 확인하기(t파일) 여기 뭐 있는지
df['키'].max()
df['키'].min()
df['키'].mean()
df['키'].count()
df['국어'].sum()
df['키'].describe()
df['키'].info()
df['키'].nlargest(3) # 키 큰 순서대로 3개 가져옴. 괄호안에 숫자 없으면 5개 가져옴
df['키'].nsmallest(3) # 키 작은 순서대로 3개 가져옴


df.describe() # 컬럼별 대략적인 정보, 최소값, 최대값, 평균 등 확인
df.head() # 상단 5개 출력
df.tail() # 하단 5개 출력
df.info() # 컬럼별 타입, 크기 정보
df.values # rows 데이터 배열로 출력
df.index # index 정보
df.columns # 컬럼 정보
df.shape # 데이터 크기


# 2개 row 데이터 출력
df.loc[['1번','5번']]
# 1번 학생의 키 값만 출력 
df.loc['1번', '키']
df.loc['1번',['이름','키']] # 1번 학생의 이름, 키 출력
df.loc[['1번','5번'],['이름','키']]
df.loc['1번':'5번', '국어':'사회']

# rows 데이터 가져오기
df[0:3]
df[5:]
# df[[0,1,3]] # error
df.iloc[[0,1,3]] # rows 데이터 부분적으로 가져오기
df.head()
df.tail(2)

# 문자열 함수
# slice(1:3)
# slcie : 문자열 자르기
df_str['idx'].str.slice(1,3)
def d_map(x):
    return x[1:3]   

df_str['idx'].map(lambda x:x[1:3]) # x: 매개변수, x[1:3] : 함수의 실행문
# df_str['idx'].map(d_map()) # map(함수) , lambda : 함수, 무명함수/익명함수

# split : 문자열 분리
a_list = ['데이터, 분석가','영희, 철수, 바둑이','국어, 영어,수학, 과학, 사회']
data={"d_split":a_list}
df_str = pd.DataFrame(data)
s_data = df_str['d_split'].str.split(',') # 배열로 분리되어 리턴
s_data

# replace : 문자열 처리, strip: 공백제거

# &, |



# 위치 지정해서 데이터를 입력하면 수정
df.iloc[0,-1] = df.iloc[0].sum()


# 총합 점수가 300점이 넘으면 합격, 
df[df['총합']>300]
df.loc[df['총합']>300,'결과'] = '합격'
df

# 학년별 인원수
school['학년'].value_counts().loc['구로고']

# 학년별 퍼센트
(school['학년'].value_counts(normalize=True).loc['구로고']*100).astype(str)+'%'


# 한 주문에 10달러 이상 사용한 주문 번호를 출력하시오. 
df_sum = df.groupby('order_id').sum()
df_sum[df_sum['item_price']>=10].sort_values('item_price', ascending=False).head()

# 5/16
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
import seaborn as sns
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # 한글설정
matplotlib.rcParams['font.size'] = 10 # 글자크기
matplotlib.rcParams['axes.unicode_minus'] = False # 마이너스 기호(-) 표기