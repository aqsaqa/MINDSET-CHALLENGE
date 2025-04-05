import streamlit as st
import datetime

# Function to get the current date
def get_current_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")

# Title of the app
st.title("Growth Mindset Challenge")

# Header for instructions
st.header("Welcome to the Growth Mindset Challenge!")

# Challenge description
st.markdown("""
This is a daily growth mindset challenge. The goal is to reflect on your thoughts, actions, and progress each day. 
Take a moment to write down your reflections and try to adopt a mindset that focuses on learning, growth, and positivity.
""")

# Display current date
st.subheader(f"Today's Date: {get_current_date()}")

# Daily Challenge
st.subheader("Today's Challenge")
challenge = "What is one thing you learned today or a challenge you overcame?"
st.write(challenge)

# User input area to reflect on the challenge
user_reflection = st.text_area("Write your reflection here:")

# Save user's reflection to a session state variable
if 'reflections' not in st.session_state:
    st.session_state.reflections = []

if st.button("Save Reflection"):
    if user_reflection:
        reflection = {
            'date': get_current_date(),
            'reflection': user_reflection
        }
        st.session_state.reflections.append(reflection)
        st.success("Reflection saved successfully!")
    else:
        st.error("Please write something before saving.")

# Display all past reflections
st.subheader("Your Past Reflections")
for reflection in st.session_state.reflections:
    st.write(f"**Date:** {reflection['date']}")
    st.write(f"**Reflection:** {reflection['reflection']}")
    st.write("---")
