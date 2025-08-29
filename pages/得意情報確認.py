import streamlit as st
import numpy as np
import pandas as pd
import json

# rはread(読む)のr
json_openfile = open('specialty.json','r',encoding='utf-8')


json_load = json.load(json_openfile)

data = []

for name, info in json_load.items():
    data.append({
        '名前': name,
        '所属': info['Affiliation'],
        'スキル': info['skill']
    })

df = pd.DataFrame(data)
st.table(df)