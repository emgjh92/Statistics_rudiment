import pandas as pd

#Anaconda Prompt 를 관리자 권한으로 실행 후 active test => conda install pandas 
#로 패키지 설치


df = pd.read_csv("../data/gapminder.tsv", sep='\t')

#print(df.head())#초반 내용 출력...

print(type(df))

print(df.shape)#출력값 : (1704, 6) ==> 가로세로 몇행몇열인지 출력

print(df.columns) 
#Index(['country', 'continent', 'year', 'lifeExp', 'pop', 'gdpPercap'], dtype='object')

print(df.columns[0])
#country

print(df.dtypes)
'''
country       object
continent     object
year           int64
lifeExp      float64
pop            int64
gdpPercap    float64
dtype: object

'''

print(df.info())


print("===========================")
#열단위로 추출하기
country_df = df['country'] #열값을 뽑아온것 = Series
print(type(country_df))
print(country_df)

print(country_df.head())
print(country_df.tail())

subset = df[['country','year','lifeExp']]

print(subset)
print(type(subset))

print("===========================")

xx = df.loc[999] #열값을 뽑아온것 = Series
print(xx)
print(type(xx))

xx = df.loc[1703] 
print(xx)

print("===========================")
xx = df.loc[df.shape[0]-1]
xx = df.iloc[-1] #loc[-1]은 불가능 (iloc 만 가능)
print(xx)

print("===========================")


xx = df.loc[[0,99,999]] #Series가 여러개 뽑혔으므로 dataFrame
print(xx)


print("===========================")

xx = df.loc[[0]]
print(type(xx))
xx = df.loc[0]
print(type(xx))

print("===========================")
xx = df.loc[0:3] #Slicing
print(xx)


 
xx = df.iloc[0]
print(xx)
print(type(xx))

xx = df.iloc[-1]
print(xx)

print("===========================")
xx = df.iloc[[0,99,-1,-2]]
print(xx)


print("===========================")
#슬라이싱 구문으로 추출하기
subset = df.loc[:,["country","year"]] #배열 행, 배열 열
#위의 경우 행 전체, 열 두개 대상 추출
print(subset)


subset = df.iloc[3:4,[0,1]]
print(subset)

subset = df.iloc[[3,4,5],[0,1]]
subset = df.iloc[99:-99,[0,1]]
subset = df.iloc[99:-99,1:-2]
print(subset)