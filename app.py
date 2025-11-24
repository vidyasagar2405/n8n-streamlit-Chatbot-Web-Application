import streamlit as st
import requests

## Title and subheader of the application.
st.title(":rainbow[🤖 ChatBot Web Application]")
st.subheader(":blue[🙋 Ask any query, Step ahead in your journey 🛫.]")

## storing the past converstion in using st.session_state
if "conversation" not in st.session_state:
    st.session_state["conversation"] = []

## user prompt
prompt= st.chat_input("Type your message here")

## webhook url from n8n
url = "https://sagardesktopn8n.app.n8n.cloud/webhook-test/5ec4cd11-ac28-4ba6-8b5a-8c552fcadd8a"

if prompt : ## if user gives any input
    st.session_state["conversation"].append({"role":"user", "data" : prompt})
    response = requests.post(url = url, json = {"prompt" : prompt}) ## request and response from n8n
    
    if response.status_code == 200 : ## if response is success with 200
        st.session_state["conversation"].append({"role":"assistant", "data" : response.json()[0]["output"]})
    else : ## else error response.
         st.session_state["conversation"].append({"role":"assistant", "data" : f"ERROR : {response.status_code}"})

#displaying the conversation with AI on the left and user on the right
for con in st.session_state["conversation"]:
    left_col, right_col = st.columns([3, 1])

    role = con.get("role")
    text = con.get("data")

    if role == "assistant":
        with left_col:
            with st.chat_message("assistant"):
                st.write(text)
    else:
        with right_col:
            with st.chat_message("user"):
                st.write(text)