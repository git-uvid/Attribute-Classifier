import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="Other Language Ignorance", layout="wide")
st.title("Other Language Ignore")

uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx", "xls"])

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)

        # Keep columns that DO NOT contain '@' in their header
        filtered_df = df.loc[:, ~df.columns.str.contains('@')]

        st.subheader("Filtered Data (Columns without '@')")
        st.dataframe(filtered_df)

        # Save filtered DataFrame to an in-memory Excel file
        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            filtered_df.to_excel(writer, index=False)
        output.seek(0)

        st.download_button(
            label="Download Filtered Excel",
            data=output,
            file_name="filtered_Dimension.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    except Exception as e:
        st.error(f"Error processing file: {e}")
