import sys
from pathlib import Path
import streamlit as st
import pandas as pd

# import your backend pipeline
from app.services.pipeline import scamguard_chain 

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(ROOT_DIR))

st.set_page_config(page_title="ScamGuard AI", layout="centered")

st.title("🚨 ScamGuard AI")
st.write("Detect scams in messages, emails, or files")

# ---- TEXT INPUT ----
user_input = st.text_area("Paste your message/email here")

# ---- FILE UPLOAD ----
uploaded_file = st.file_uploader("Or upload a CSV or Excel file", type=["csv", "xlsx"])

input_text = ""

if uploaded_file is not None:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.write("Preview:")
    st.dataframe(df.head())

    results = []

    if df is not None:
        column = st.selectbox("Select column to analyze", df.columns)


#  ---- RUN BUTTON-----
if st.button("Analyze File", key="analyze_file_btn") and df is not None:
    progress = st.progress(0)
    results = []

    for i, row in df.iterrows():
        text = str(row[column])

        if text.strip():
            result = scamguard_chain.invoke(text)
            results.append(result)
        else:
            results.append(None)

        progress.progress((i + 1) / len(df))

    # 👇 SHOW RESULTS HERE (IMPORTANT)
    df["is_scam"] = [r["is_scam"] if r else None for r in results]
    df["risk_level"] = [r["risk_level"] if r else None for r in results]
    df["confidence"] = [r["confidence_score"] if r else None for r in results]

    st.success("Analysis Complete")
    st.dataframe(df)
elif user_input:
    input_text = user_input

# ---- RUN BUTTON ----
if st.button("Analyze", key="analyze_text_btn"):

    if not input_text.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("Analyzing..."):
            try:
                result = scamguard_chain.invoke(input_text)

                st.success("Analysis Complete")
                print(f"result: {result}")

                # Pretty output
                st.json(result)

            except Exception as e:
                st.error(f"Error: {str(e)}")