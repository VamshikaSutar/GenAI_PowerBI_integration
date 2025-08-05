import streamlit as st
import pandas as pd
from backend.client_manager import ClientManager
from backend.file_utils import read_excel, get_excel_sheets
# Init client
# client = ClientManager()

# st.title("Client Dashboard Chatbot")

# Removed PowerBI section for now
# st.subheader("🔗 PowerBI Dashboard")
# st.markdown(f"[View Dashboard]({client.get_powerbi_url()})", unsafe_allow_html=True)


# Show Excel data
# excel_path = 'data/client_abc.xlsx'
# st.subheader("📄 Client Data Preview")
# df = read_excel(excel_path)
# if df is not None:
#     st.dataframe(df)


# else:
#     st.error("Failed to load Excel file.")


client = ClientManager()
excel_path = client.get_excel_path()

# PowerBI embedding through backend
powerbi_url = client.get_powerbi_url()

if powerbi_url:
    st.subheader("Power BI Report")
    st.markdown(
        f"""
       iframe title="PBI_testing1" width="100%" height="800" src="{powerbi_url}"></iframe>
        """,
        unsafe_allow_html = True
)

# st.title("Client Dashboard Chatbot")

# if excel_path:
#     sheet_names = get_excel_sheets(excel_path)
#     if sheet_names:
#         selected_sheet = st.selectbox("Select a sheet to load", sheet_names)

#         df = read_excel(excel_path, selected_sheet)

#         if df is not None and not df.empty:
#             st.subheader("Full Data Preview")
#             st.dataframe(df)

#             selected_columns = st.multiselect("Select Column for Analysis", df.columns.tolist())

#             if selected_columns:
#                 st.subheader("Selected Column Data Preview")
#                 st.dataframe(df[selected_columns])
#         else:
#             st.error("Failed to load sheet or its empty")

#     else:
#         st.error("No sheets found in Excel file")
# else:
#     st.error("Excel file path not found")

