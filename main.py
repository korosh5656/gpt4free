# pip install -U g4f
# pip install PyExecJS
# pip install streamlit


import streamlit as st

st.title('my chatbot (tarfandoon)')

inp = st.text_area('هر سوالی دارید بپرسید')
ok = st.button('Lets Go')

if inp and ok:
    try:
        import g4f
        response = g4f.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{"role": "user", "content": inp}],
            stream=True
        )
        # نمایش نتایج
        for message in response:
            st.write(message['content'])  # فرض بر اینکه پیام‌ها در کلید 'content' هستند.
    except Exception as e:
        st.error(f"خطا رخ داده است: {e}")
