import streamlit as st
from capture_face import capture_face
from recognize_face import recognize_face
from log_access import log_entry

st.title("AI-Powered Face Recognition Security System")

action = st.radio("Select Action:", ["Register Face", "Authenticate"])

if action == "Register Face":
    user_name = st.text_input("Enter Your Name:")
    if st.button("Capture Face"):
        capture_face(user_name)
        st.success(f"Face registered for {user_name}")

elif action == "Authenticate":
    if st.button("Start Face Recognition"):
        user = recognize_face()
        if user:
            st.success(f"Welcome, {user}!")
            log_entry(user, "Access Granted")
        else:
            st.error("Access Denied!")
