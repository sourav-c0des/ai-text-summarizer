# frontend/app.py

import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/summarize"

# Page configuration
st.set_page_config(page_title="AI Text Summarizer", layout="wide")

# Title
st.title("🧠 AI Text Summarizer")
st.write(
    "Paste your text below and generate a concise summary. Choose between short, "
    "medium, or detailed summaries — no technical settings needed."
)

# Sidebar — Simple Summary Length Selector
st.sidebar.header("Summary Settings")

summary_level = st.sidebar.selectbox(
    "Summary Length",
    ["Short", "Medium", "Long"],
    index=1
)

# Map Summary Level -> Model Parameters
if summary_level == "Short":
    max_len = 60
    min_len = 20
elif summary_level == "Medium":
    max_len = 120
    min_len = 40
else:  # Long
    max_len = 200
    min_len = 80

# Text input field
text_input = st.text_area(
    "Enter your text here:",
    height=250,
    placeholder="Paste an article, document, essay, paragraph...",
)

# Summarize button
if st.button("Summarize"):
    if not text_input.strip():
        st.warning("Please enter some text before summarizing.")
    else:
        with st.spinner("Generating summary… please wait…"):
            try:
                payload = {
                    "text": text_input,
                    "max_length": max_len,
                    "min_length": min_len,
                }
                response = requests.post(API_URL, json=payload)

                if response.status_code == 200:
                    data = response.json()

                    # Display Summary
                    st.subheader("Summary")
                    st.write(data["summary"])

                    # Display Stats
                    st.subheader("Stats")
                    col1, col2 = st.columns(2)
                    col1.metric(
                        "Original Text Size",
                        f"{data['original_length']} characters"
                    )
                    col2.metric(
                        "Summary Size",
                        f"{data['summary_length']} characters"
                    )
                else:
                    st.error(f"API Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"Request failed: {e}")
