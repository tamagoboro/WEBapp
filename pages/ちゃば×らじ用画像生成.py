import streamlit as st
from PIL import Image,ImageDraw,ImageFont


st.caption('ちゃば×らじの質問画像生成アプリ')

texttitle = st.text_input('質問を入力してください:','',width=20)
textname = st.text_input('ラジオネームを入力してください:','',width=20)

img = Image.open('ragi.png')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('meiryo.ttc',40)

draw.text((50,50),texttitle,fill=(255,0,0),font=font)
draw.text((80,50),texttitle,fill=(255,0,0),font=font)

# 表示
st.image(img, caption="文字を書き込んだ画像")

# 保存ボタン
if st.button("保存する"):
    img.save(f"output{textname}.jpg")
    st.success(f"保存しました！（output{textname}.jpg）")