import streamlit as st
import numpy as np
import pandas as pd
import json

# rはread(読む)のr
json_openfile = open('specialty.json','r',encoding='utf-8')


json_load = json.load(json_openfile)

for name , info in json_load.values():

    df =pd.DataFrame({
        '名前':[name],
        '所属':{info['Affiliation']},
        'スキル':{info['skill']}
    })
    st.table(df.style.highlight_max(axis=0))
    st.write(df)