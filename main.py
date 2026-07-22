import streamlit as st
import os
import pandas as pd

########### Streamline dataflow #########################
# print('Run')
# pressed = st.button("Press me!")
# print("first:", pressed)

# pressed2 = st.button("Press me2!")
# print("second:", pressed2)

################ Text elements #########################
# st.title("Super Cool Streamlit App")
# st.header("This is a header")
# st.subheader("This is a subheader")
# st.markdown("This is a _markdown_ text")
# st.caption("This is a caption")

# code = """
# def hello():
#     print("Hello, World!")
# """
# st.code(code, language="python")

# st.divider()

# st.image(os.path.join(os.getcwd(), "static", "background.jpg"), caption="Streamlit Logo")

############# Data elements   ####################

st.title("Data Elements in Streamlit")

#DataFrame
st.subheader("DataFrame Example")
df = pd.DataFrame({
    'NAME': ["Shristi", "Shreeya ", "Om", "Atul"],
    'AGE': ['29', '30', '24', '16']
})

st.dataframe(df)

#Data Editor Section (Editable DataFrame)
st.subheader("Data Editor Example")
editable_df = st.data_editor(df)
print("Editable DataFrame:", editable_df)

#Static Table Section
st.subheader("Static Table Example")
st.table(df)

#Metric Section
st.subheader("Metric Example")
st.metric(label="Total Rows", value= len(df), delta=0)
st.metric(label="Average Age", value= round(df['AGE'].astype(int).mean(), 1), delta=1)

#JSON and Dict Section
st.subheader("JSON and Dict Example")
sample_dict = {
    "name": "Shristi",
    "age": 29,
    "city": "Kathmandu"
}
st.json(sample_dict)

#Also, show it as dictionary
st.write("Dictionary View:", sample_dict)





