import streamlit as st
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

from datetime import datetime

min_date = datetime(1900, 1, 1)
max_date = datetime.now()

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

# st.title("Data Elements in Streamlit")

# #DataFrame
# st.subheader("DataFrame Example")
# df = pd.DataFrame({
#     'NAME': ["Shristi", "Shreeya ", "Om", "Atul"],
#     'AGE': ['29', '30', '24', '16']
# })

# st.dataframe(df)

# #Data Editor Section (Editable DataFrame)
# st.subheader("Data Editor Example")
# editable_df = st.data_editor(df)
# print("Editable DataFrame:", editable_df)

# #Static Table Section
# st.subheader("Static Table Example")
# st.table(df)

# #Metric Section
# st.subheader("Metric Example")
# st.metric(label="Total Rows", value= len(df), delta=0)
# st.metric(label="Average Age", value= round(df['AGE'].astype(int).mean(), 1), delta=1)

# #JSON and Dict Section
# st.subheader("JSON and Dict Example")
# sample_dict = {
#     "name": "Shristi",
#     "age": 29,
#     "city": "Kathmandu"
# }
# st.json(sample_dict)

# #Also, show it as dictionary
# st.write("Dictionary View:", sample_dict)

############# Chart elements   ####################

# st.title("Chart Elements in Streamlit")

# #Generate small sample data
# data = pd.DataFrame(np.random.randn(20,3),
#                      columns=['A', 'B', 'C'])

# #Area Chat Section
# st.subheader("Area Chart Example")
# st.area_chart(data)

# #Bar Chart Section
# st.subheader("Bar Chart Example")
# st.bar_chart(data)

# #Line Chart Section
# st.subheader("Line Chart Example")
# st.line_chart(data)


# #Scatter Chart Section
# st.subheader("Scatter Chart Example")
# scatter_data = pd.DataFrame(np.random.randn(100, 2), columns=['x', 'y'])
# st.scatter_chart(scatter_data)

# #Map Section
# st.subheader("Map Example") 
# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon'])
# st.map(map_data)

# #pyplot Section
# st.subheader("Pyplot Example")
# fig, ax = plt.subplots()
# ax.plot(data['A'], data['B'], '-o')
# ax.set_xlabel('A')
# ax.set_ylabel('B')
# st.pyplot(fig)


############## Form elements ####################
# st.title("Form Elements in Streamlit")
# st.title("Form Elements in Streamlit")

# # Form to hold the interactive elements
# with st.form(key='my_form'):
#     # Text Input
#     st.subheader("Text Input Example")
#     name = st.text_input("Enter your name")
#     feedback = st.text_area("Enter your feedback")

#     # Number Input
#     st.subheader("Number Input Example")
#     age = st.number_input("Enter your age", min_value=0, max_value=120, step=1)
#     time_spent = st.time_input("Select the time spent on the app", value=pd.Timestamp.now().time())

#     # Selectbox
#     st.subheader("Selectbox Example")
#     gender = st.selectbox("Select your gender", ["Male", "Female", "Other"])
#     choice = st.selectbox("Select your favorite programming language", ["Python", "JavaScript", "C++", "Java", "Other"])  
#     slider_value = st.slider("Select a value", min_value=0, max_value=100, value=50) 

#     #toggles and checkboxes
#     st.subheader("Toggle and Checkbox Example")
#     toggle = st.checkbox("Enable feature X")
#     checkbox = st.checkbox("Subscribe to newsletter")

#     #Summit button
#     submit_button = st.form_submit_button(label='Submit')

# #oUTSIDE THE FORM
# st.subheader("Form Submission Result")
# if st.button("Submit Form"):
#     if submit_button:
#         st.write("Form submitted successfully!")
#         st.write(f"Name: {name}")
#         st.write(f"Feedback: {feedback}")
#         st.write(f"Age: {age}")
#         st.write(f"Time Spent: {time_spent} minutes")
#         st.write(f"Gender: {gender}")
#         st.write(f"Favorite Programming Language: {choice}")


##########Simple Form Example#####################
# st.title("User Information Form")

# form_values = {
#     "name": None,
#     "height": None,
#     "gender": None,
#     "dob": None
# }

# with st.form(key="user_info_form"):
#     form_values["name"] = st.text_input("Enter your name: ")
#     form_values["height"] = st.number_input("Enter your height (cm): ")
#     form_values["gender"] = st.selectbox("Gender", ["Male", "Female"])
#     form_values["dob"] = st.date_input("Enter your birthdate")

#     submit_button = st.form_submit_button(label="Submit")

#     if submit_button:
#         if not all(form_values.values()):
#             st.warning("Please fill in all of the fields")
#         else:
#             st.balloons()
#             st.write("### Info")
#             for (key, value) in form_values.items():
#                 st.write(f"{key}: {value}")    

############ Advanced Form Example #####################
# st.title("Advanced User Information Form")


# with st.form(key="user_info_form", clear_on_submit=True):
#     name1 = st.text_input("Enter your first name")

#     birth_date = st.date_input(
#         "Enter your birth date",
#         min_value=min_date,
#         max_value=max_date
#     )

#     if birth_date:
#         age = max_date.year - birth_date.year

#         if (
#             birth_date.month > max_date.month or
#             (
#                 birth_date.month == max_date.month and
#                 birth_date.day > max_date.day
#             )
#         ):
#             age -= 1

#         st.write(f"Your calculated age is {age} years")

#     submit_button1 = st.form_submit_button(label="Submit Form")

#     if submit_button1:
#         if not name1 or not birth_date:
#             st.warning("Please fill in all form inputs")
#         else:
#             st.success(f"Thank you, {name1}. Your age is {age}.")
#             st.balloons()

############ Sesion State Example #####################
# if "counter" not in st.session_state:
#     st.session_state.counter = 0

# if st.button("Increment Counter"):
#     st.session_state.counter += 1
#     st.write(f"Counter incremented to {st.session_state.counter}")

# if st.button("Reset"):
#     st.session_state.counter = 0
# else:
#     st.write("Counter did not reset")

# st.write(f"Counter value: {st.session_state.counter}")

############ Call backs Example #####################

# if "step" not in st.session_state:
#     st.session_state.step = 1

# if "info" not in st.session_state:
#     st.session_state.info = {}

# def go_to_step2(name):
#     st.session_state.info["name"] = name
#     st.session_state.step = 2

# def go_to_step1():
#     st.session_state.step = 1   


# if st.session_state.step == 1:
#     st.header("Part 1: Info")

#     name = st.text_input("Name", value=st.session_state.info.get("name", ""))

#     st.button("Next", on_click=go_to_step2, args=(name,))
     

# if st.session_state.step == 2:
#     st.header("Part 2: Review")

#     st.subheader("Please review this:")
#     st.write(f"**Name**: {st.session_state.info.get('name', '')}")

#     if st.button("Submit"):
#         st.success("Great!")
#         st.balloons()
#         st.session_state.info = {}

#     st.button("Back", on_click=go_to_step1)

############### Layouts Example #####################

# # Sidebar layout
# st.sidebar.title("This is the Sidebar")
# st.sidebar.write("You can place elements like sliders, buttons, and text here.")
# sidebar_input = st.sidebar.text_input("Enter something in the sidebar")

# # Tabs layout
# tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

# with tab1:
#     st.write("You are in Tab 1")

# with tab2:
#     st.write("You are in Tab 2")

# with tab3:
#     st.write("You are in Tab 3")

# # Columns layout
# col1, col2 = st.columns(2)
# with col1:
#     st.header("Column 1")
#     st.write("Content for column 1")
# with col2:
#     st.header("Column 2")
#     st.write("Content for column 2")

# # Containers example
# with st.container(border=True):
#     st.write("This is inside a container.")
#     st.write("You can think of containers as a grouping for elements.")
#     st.write("Containers help manage sections of the page.")

# # Empty placeholder
# placeholder = st.empty()
# placeholder.write("This is an empty placeholder, useful for dynamic content.")

# if st.button("Update Placeholder"):
#     placeholder.write("The content of this placeholder has been updated.")

# # Expander
# with st.expander("Expand for more details"):
#     st.write("This is additional information that is hidden by default.")
#     st.write("You can use expanders to keep your interface cleaner.")

# # Popover (Tooltip)
# st.write("Hover over this button for a tooltip")
# st.button("Button with Tooltip", help="This is a tooltip or popover on hover.")

# # Sidebar input handling
# if sidebar_input:
#     st.write(f"You entered in the sidebar: {sidebar_input}")

############### Addvance widgets Example ####################

# if "slider" not in st.session_state:
#     st.session_state.slider = 25

# min_value = st.slider("Set min value", 0, 50, 25)

# st.session_state.slider = st.slider("Slider", min_value, 100, st.session_state.slider)

###########################
# if "checkbox" not in st.session_state:
#     st.session_state.checkbox = False

# def toggle_input():
#     st.session_state.checkbox = not st.session_state.checkbox

# st.checkbox("Show Input Field", value=st.session_state.checkbox, on_change=toggle_input)

# if st.session_state.checkbox:
#     user_input = st.text_input("Enter something:", value=st.session_state.get("user_input", ""))
#     st.session_state.user_input = user_input
# else:
#     user_input = st.session_state.get("user_input", "")

# st.write(f"User Input: {user_input}")

################### Caching Example ####################
# @st.cache_data(ttl=60)  # Cache this data for 60 seconds
# def fetch_data():
#     # Simulate a slow data-fetching process
#     time.sleep(3)  # Delays to mimic an API call
#     return {"data": "This is cached data!"}

# st.write("Fetching data...")
# data = fetch_data()
# st.write(data)


# file_path = "example.txt"

# @st.cache_resource
# def get_file_handler():
#     # Open the file in append mode, which creates the file if it doesn't exist
#     file = open(file_path, "a+")
#     return file

# # Use the cached file handler
# file_handler = get_file_handler()

# # Write to the file using the cached handler
# if st.button("Write to File"):
#     file_handler.write("New line of text\n")
#     file_handler.flush()  # Ensure the content is written immediately
#     st.success("Wrote a new line to the file!")

# # Read and display the file contents
# if st.button("Read File"):
#     file_handler.seek(0)  # Move to the beginning of the file
#     content = file_handler.read()
#     st.text(content)

# # Always make sure to close the file when done (useful for resource cleanup)
# st.button("Close File", on_click=file_handler.close)

###################### Rerun Example ####################

# st.title("Counter Example with Immediate Rerun")

# if "count" not in st.session_state:
#     st.session_state.count = 0
    

# def increment_and_rerun():
#     st.session_state.count += 1
#     st.rerun()

# st.write(f"Current Count: {st.session_state.count}")

# if st.button("Increment and Update Immediately"):
#     increment_and_rerun()


################# Fragments Example ####################
st.title("My Awesome App")

@st.fragment()
def toggle_and_text():
    cols = st.columns(2)
    cols[0].toggle("Toggle")
    cols[1].text_area("Enter text")


@st.fragment()
def filter_and_file():
    new_cols = st.columns(5)
    new_cols[0].checkbox("Filter")
    new_cols[1].file_uploader("Upload image")
    new_cols[2].selectbox("Choose option", ["Option 1", "Option 2", "Option 3"])
    new_cols[3].slider("Select value", 0, 100, 50)
    new_cols[4].text_input("Enter text")


toggle_and_text()
cols = st.columns(2)
cols[0].selectbox("Select", [1, 2, 3], None)
cols[1].button("Update")
filter_and_file()
