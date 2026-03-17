# Streamlit常见组件及其使用方法

## st.header标题

```
streamlit.header(body)
```

body：标题字符串。

## st.markdown

```
st.markdown(body, unsafe_allow_html=False)
```

body：要显示的markdown文本，字符串。

unsafe_allow_html： 是否允许出现html标签，布尔值，**默认：false**，表示所有的html标签都将转义。 **注意，这是一个临时特性，在将来可能取消。**

## st.write段落

```
st.write(*args, **kwargs)
```

*args：一个或多个要显示的对象参数。

unsafe_allow_html ：是否允许不安全的HTML标签，布尔类型，默认值：false。

## st.button按钮

```
st.button(label, key=None)
```

label：按钮提示文本。

key：按钮组件的键，可选。如果未设置的话，streamlit将自动生成一个唯一键。

## st.radio单选

```
st.radio(label, options, index=0, format_func=<class 'str'>, key=None)
```

label：选择题题目。

options：选项列表，可以是以下类型： list tuple numpy.ndarray pandas.Series

```
st.radio("选择一个选项", ("1、是", "2、不是", "3、不清楚"))
```

![image-20260317210621981](D:\虚拟教育\虚拟课堂\CyberClassroom-Streamlit\Streamlit常见组件及其使用方法.assets\image-20260317210621981.png)

index：选中项的序号，整数。

format_func：选项文本的显示格式化函数。

key：组件ID，当未设置时，streamlit会自动生成。

## st.sidebar滑动条

```
st.slider(label, min_value=None, max_value=None, value=None, step=None, format=None, key=None)
```

label：说明文本，字符串。

min_value：允许的最小值，默认值：0或0.0。

max_value：允许的最大值，默认值：0或0.0。

value：当前值，默认值为min_value。

step：步长，默认值为1或0.01。

format：数字显示格式字符串 。

key：组件ID。

```
# 交互式滑块
x = st.slider("选择一个数字", 0.0, 100.0, 50.0)
st.write(f"你选择的数字是: {x}")
```

![image-20260317210925169](D:\虚拟教育\虚拟课堂\CyberClassroom-Streamlit\Streamlit常见组件及其使用方法.assets\image-20260317210925169.png)

## st.empty

```
st.empty()
```

填充占位符。

> 尚未知其作用

## st.columns表格列（？

插入并排排列的容器。

```
st.columns(spec, *, gap="small")
```

spec: 控制要插入的列数和宽度。

gap: 列之间的间隙大小。

```
st.columns(3)  # 创建三列
col1, col2, col3 = st.columns(3)
with col1:
    st.write("这是第一列") 
with col2:
    st.write("这是第二列")
with col3:
    st.write("这是第三列")
```

![image-20260317211044383](D:\虚拟教育\虚拟课堂\CyberClassroom-Streamlit\Streamlit常见组件及其使用方法.assets\image-20260317211044383.png)