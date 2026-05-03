import streamlit as st


# 1. trying out widget of streamlit framework
# st.title("Playing with widget")
# name = st.text_input("Enter your name")
# age = st.slider("Select your age", 0, 100, 25)
# if(st.button("Submit")):
#     st.write(f'Hello {name}!')
#     st.write(f'your age is: {age}')


# 2. TRYING IT OUT USING COLUMNS

# col1, col2 = st.columns(2)
# with col1:
#     name = st.text_input("Enter your name")
# with col2:
#     age = st.slider("Enter your age", 0, 100, 25)

# if(st.button("Submit")):
#     st.write(f"Hello {name}")
#     st.write(f"you are {age} years old")

# 3. Widget - Expander 
# st.title("Widget playground th Expanders")

# # Expander for Personal details
# with st.expander("📇 Personal Details"):
#     name = st.text_input("Enter your name ?")
#     age = st.slider("Enter your age", 0, 100, 25)

# # Expander for preferences
# with st.expander("⚙️ Preferences"):
#     color = st.selectbox("Choose your favorite color: ", ["Red", "Green", "Blue"])
#     subscribe = st.checkbox("Subscribe to newsletter")

# # Expander for Submission
# with st.expander("🚀 Submit"):
#     if(st.button("Submit")):
#         st.write(f"Hello {name}, you are {age} years old")
#         st.write(f"your favourite color: {color}")
#         if subscribe:
#             st.success("You are subscribed to newletter 🎉")
#         else:
#             st.info("You are not subscriber!")



# 4. Tabs
st.title("Playing with widgets: Tabs")

# Create Tabs
tab1, tab2, tab3 = st.tabs(["💁🏻 Personal Details", "⚙️ Preferences", "🚀 Submit"])

# Tab-1: Personal Details
with tab1:
    name = st.text_input("Wnter your name ?")
    age = st.slider("What is you age ?", 0, 100, 25)

#  Tab-2: Preferences:
with tab2:
    color = st.selectbox("Choose your theme color: ", ["Red", "Blue", "Dark", "Purple"])
    subscribe = st.checkbox("Subscribe to Newsletter")

# Tab - 3: Submit
with tab3:
    if(st.button("Submit")):
        st.write(f"Hello {name}, you are {age} years old.")
        st.write(f"Your theme for our application is: {color}")
        if subscribe:
            st.success("You are subscribed to our newsletter!🎉")
        else:
            st.info("You are not subscriber!")

