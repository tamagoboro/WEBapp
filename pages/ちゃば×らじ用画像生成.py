import streamlit as st
from PIL import Image,ImageDraw,ImageFont


st.caption('ちゃば×らじの質問画像生成アプリ')

texttitle = st.text_input('質問を入力してください:','',width=300)
textname = st.text_input('ラジオネームを入力してください:','',width=300)

img = Image.open('ragi.png')
draw = ImageDraw.Draw(img)
fonttitle = ImageFont.truetype('YDWaosagi.otf', 150)
font = ImageFont.truetype('YDWaosagi.otf', 80)

draw.text((1024, 750), texttitle, fill=(0,0,0), font=fonttitle, anchor="mm")
draw.text((1024,950),f"ラジオネーム:{textname}",fill=(0,0,0),font=font,anchor="mm")

# 表示
st.image(img, caption="文字を書き込んだ画像")

# 保存ボタン
if st.button("保存する"):
    img.save(f"output{textname}.jpg")
    st.success(f"保存しました！（output{textname}.jpg）")