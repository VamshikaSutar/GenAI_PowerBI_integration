import streamlit as st
from backend.client_manager import ClientManager
from backend.file_utils import read_excel
# Init client
client = ClientManager()

st.title("Client Dashboard Chatbot")

# Removed PowerBI section for now
# st.subheader("🔗 PowerBI Dashboard")
# st.markdown(f"[View Dashboard]({client.get_powerbi_url()})", unsafe_allow_html=True)


# Show Excel data
excel_path = 'data/client_abc.xlsx'
st.subheader("📄 Client Data Preview")
df = read_excel(excel_path)
if df is not None:
    st.dataframe(df)
else:
    st.error("Failed to load Excel file.")
