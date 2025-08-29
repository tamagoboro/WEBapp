import streamlit as st
from PIL import Image,ImageDraw,ImageFont
import textwrap
import io

st.caption('ちゃば×らじの質問画像生成アプリ')

texttitle = st.text_input('質問を入力してください:','',width=300)

wrapped_text = "\n".join(textwrap.wrap(texttitle, 20))
textname = st.text_input('ラジオネームを入力してください:','',width=300)

img = Image.open('ragi.png')
draw = ImageDraw.Draw(img)
fonttitle = ImageFont.truetype('YDWaosagi.otf', 90)
font = ImageFont.truetype('YDWaosagi.otf', 60)

draw.text((1024, 650),  wrapped_text,  fill=(0,0,0), font=fonttitle, anchor="mm")
draw.text((1024,950),f"ラジオネーム:{textname}",fill=(0,0,0),font=font,anchor="mm")

# 表示
st.image(img, caption="文字を書き込んだ画像")

# 保存ボタン
# 保存ボタン
if st.button("保存する"):
    buf = io.BytesIO()
    if img.mode == "RGBA":
        img = img.convert("RGB")
    img.save(buf, format="JPEG")
    st.download_button("画像をダウンロード", data=buf.getvalue(), file_name="output.jpg", mime="image/jpeg")
