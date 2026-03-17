import streamlit as st

# 页面标题
st.title("我的第一个Streamlit应用")

# 文本
st.write("这是一个用Python创建的网页前端！")

# 交互式滑块
x = st.slider("选择一个数字", 0, 100, 50)
st.write(f"你选择的数字是: {x}")

# 显示数据的平方
st.write(f"{x} 的平方是: {x * x}")