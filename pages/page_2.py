import statistics as st

with st.form(key='profile_form'):
    name = st.text_input('名前')

    age = st.radio(
        '年齢層',
        ('18歳以上','18歳未満')
    )

    hobby = st.multiselect(
        '趣味',
        ('スポーツ','読書','プログラミング')
    )

    btn = st.form_submit_button('送信')
    btn2 = st.form_submit_button('キャンセル')
    if btn:
        st.caption(name)