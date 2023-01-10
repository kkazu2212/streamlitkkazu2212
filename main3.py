import streamlit as st
import time
import pandas as pd

#セレクトボックス
month = st.sidebar.selectbox(
    '月は？',
    list(range(1, 13))
)

st.title('勤務表')

df_csv = pd.read_csv((f'kinmudata\data_{month}.csv'), encoding = 'utf-8')
df_csv = df_csv.fillna('欠')
df_csv = df_csv.rename(columns={
    '1':int('1'),
    '2':int('2'),
    '3':int('3'),
    '4':int('4'),
    '5':int('5'),
    '6':int('6'),
    '7':int('7'),
    '8':int('8'),
    '9':int('9'),
    '10':int('10'),
    '11':int('11'),
    '12':int('12'),
    '13':int('13'),
    '14':int('14'),
    '15':int('15'),
    '16':int('16'),
    '17':int('17'),
    '18':int('18'),
    '19':int('19'),
    '20':int('20'),
    '21':int('21'),
    '22':int('22'),
    '23':int('23'),
    '24':int('24'),
    '25':int('25'),
    '26':int('26'),
    '27':int('27'),
    '28':int('28'),
    '29':int('29'),
    '30':int('30')
})

d_num = len(df_csv.columns)

#セレクトボックス
date = st.sidebar.selectbox(
    '日にちは？',
    list(range(1, d_num -2))
)

Class = st.sidebar.selectbox(
    '氏名は？',
    df_csv['氏名'].unique()
)

df_csv = df_csv.set_index(['氏名'])
num = df_csv.index.get_loc(Class)
df_kinmu = pd.DataFrame(df_csv.iloc[num, [0, date]])

st.write(f'{Class}')
st.write(f'{month}月')
st.write(f'{date}日')
st.write(f'勤務は{df_csv.iloc[num, date]}です。')
st.dataframe(df_kinmu)
