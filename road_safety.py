from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import google.generativeai as genai
import os

api_key = os.getenv("AIzaSyAIa7WCSFczDwkaY3XoiZBwFKiaA9rS1jk")

if not api_key:
    st.error("❌ API Key not found! Please set the GOOGLE_API_KEY environment variable.")
    st.stop()

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

def get_road_safety_tips(user_query):
    chat = model.start_chat(history=[
        {"role": "system", "parts": ["You are an AI assistant working like a road safety chatbot. Respond strictly in bullet points only."]}
    ])
    response = chat.send_message(user_query, generation_config={"temperature": 0.4})
    return response.text

st.set_page_config(page_title="🚦 Road Safety Chatbot", page_icon="🛣️")

st.title("🛣️ Road Safety Chatbot")
st.markdown("Ask any question related to road safety and get answers in clear bullet points.")

# Input box
user_input = st.text_input("📩 Enter your road safety question:")

# Submit button
# Submit button
if st.button("🚦 Get Safety Tips"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a valid question.")
    else:
        with st.spinner("Thinking... 🤔"):
            try:
                response = get_road_safety_tips(user_input)
                st.markdown("### ✅ Road Safety Guidelines:")
                st.markdown(response)
            except Exception as e:
                st.error(f"An error occurred: {e}")
