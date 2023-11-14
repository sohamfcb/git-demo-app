import streamlit as st

st.title('Messi')

col1,col2=st.columns(2)

with col1:
    st.image('Inter_Miami_Messi_Soccer_25995.jpg')

with col2:
    st.write('''He was beautiful. He was the point of difference, he has always been the point of difference. Unparalleled. And maybe today there will of course always be those who argue, always be those who debate. And the debate can rage on if you like, but as he falls in love with the object in the world that his heart most desired, it’s hard to escape the supposition that he has rendered himself today, the 𝗚𝗥𝗘𝗔𝗧𝗘𝗦𝗧 𝗢𝗙 𝗔𝗟𝗟 𝗧𝗜𝗠𝗘.''')

st.header('Courses Offered')

st.subheader('Data Science & Machine Learning')
st.subheader("Data Analysis")
st.subheader("Machine Learning")
st.subheader("Deep Learning")
st.subheader("DSA")

st.sidebar.title('Menu')

st.sidebar.markdown('''
- Home
- About
- Checkout
- Career Section
- Login 
''')

st.sidebar.selectbox('Select One',['Teacher','Student'])
st.sidebar.button('Select')

st.title('Hello Teacher')