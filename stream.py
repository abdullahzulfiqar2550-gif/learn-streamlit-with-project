import streamlit as st
import pandas as pd
import numpy as np
import time

st.title("Muhammad Abdullah AI Engineer (Title)")
st.header("Muhammad Abdullah AI Engineer (Header)")
st.subheader("Muhammad Abdullah AI Engineer (Subheader)")
st.write("Muhammad Abdullah AI Engineer (Write)")
st.markdown("Muhammad Abdullah AI Engineer (Markdown)")
st.caption("Muhammad Abdullah AI Engineer (Caption)")

st.image("C:\\Users\\Abdul\\OneDrive\\Pictures\\Screenshots\\Screenshot 2026-03-27 211238.png")
st.video("C:\\Users\\Abdul\\Videos\\Screen Recordings\\python programming.mp4")

st.checkbox("Check Button")
st.button("Click Button")
st.radio("Select Your City", ["Karachi", "Lahore", "Islamabad"])
st.selectbox("Select Your City", ["Karachi", "Lahore", "Islamabad"])
st.multiselect("Select Your City", ["Karachi", "Lahore", "Islamabad"])
st.select_slider("Select Your City", ["Good", "Average", "Bad"])
st.slider("Your Marks", 0, 100)

on = st.toggle("Activate Features")
if on:
    st.write("Features Activated")

number = st.number_input("Insert a Number")
st.write("The Current Number is", number)

d = st.date_input("When's your birthday", value=None)
st.write("your Birthday is:", d)

t = st.time_input("Set an Alarm", value=None)
st.write("Alarm is set for:", t)

st.number_input('Enter your marks', 0,100)
st.text_input('Enter Text')
st.date_input('Exam date')
st.time_input('Exam time')
st.text_area('Description')
st.file_uploader('Upload File')
st.color_picker('Choose a color')

st.success("Success")
st.error("Error")
st.warning("Warning")
st.info("Information")
st.exception(RuntimeError("RuntimeError exception"))

st.sidebar.title("Muhammad Abdullah AI Engineer (Title)")
st.sidebar.image("C:\\Users\\Abdul\\OneDrive\\Pictures\\Screenshots\\Screenshot 2026-03-27 211238.png")

df = pd.DataFrame(np.random.randn(10, 5), columns=('col %d' % i for i in range(5)))
st.dataframe(df)


df = pd.DataFrame(
    np.random.randn(10, 5), columns=("col %d" % i for i in range(5))
)
st.table(df)

col1,col2,col3=st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

prompt = st.chat_input("Ask me anything")
if prompt:
    st.write("User:", prompt)    
    

with st.status("Step 1"):
    st.write("Step 2")
    time.sleep(1)
    st.write("Step 3")
    time.sleep(1)
    st.write("Step 4")
    time.sleep(1)
st.button("Rerun")

chart_data=pd.DataFrame(np.random.randn(20,3), columns=["a", "b", "c"])
st.area_chart(chart_data)

chart_data1 = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.bar_chart(chart_data1)

chart_data2 = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.line_chart(chart_data2)

chart_data = pd.DataFrame(np.random.randn(20,3), columns=["a", "b", "c"])
df = pd.DataFrame({"lat": [31.4806], "lon": [74.3212]})
st.map(df)

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.scatter_chart(chart_data)

with st.chat_message("user"):
    st.write("Hello ji")





