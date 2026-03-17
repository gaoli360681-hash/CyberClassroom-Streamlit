import streamlit as st

# 页面标题
st.title("我的第一个Streamlit应用")

# 文本
st.write("这是一个用Python创建的网页前端！")

# 交互式滑块
x = st.slider("选择一个数字", 0.0, 100.0, 50.0)
st.write(f"你选择的数字是: {x}")

# 显示数据的平方
st.write(f"{x} 的平方是: {x * x}")

# 按钮
if st.button("点击我！"):
    st.write("按钮被点击了！")

# 单选
st.radio("选择一个选项", ("1、是", "2、不是", "3、不清楚"))

st.columns(3)  # 创建三列
col1, col2, col3 = st.columns(3)
with col1:
    st.write("这是第一列") 
with col2:
    st.write("这是第二列")
with col3:
    st.write("这是第三列")
