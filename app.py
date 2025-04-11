import streamlit as st
from style import set_page_config, apply_custom_styles
from database import save_entry, load_entries
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO

set_page_config()
apply_custom_styles()

st.title("📝 Simple Data Entry App")

# --- Form to enter new data ---
with st.form("entry_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    age = st.number_input("Age", min_value=0, max_value=120)
    notes = st.text_area("Notes")
    submitted = st.form_submit_button("Save Entry")

    if submitted:
        save_entry(name, email, age, notes)
        st.success("✅ Entry saved successfully!")

# --- Load and Prepare Data ---
entries = load_entries()
df = pd.DataFrame(entries)

if not df.empty:
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    st.subheader("📊 Dashboard")

    # --- Search and Filter ---
    search_query = st.text_input("🔍 Search by Name")
    if search_query:
        df = df[df['name'].str.contains(search_query, case=False)]

    # --- Stats ---
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Entries", len(df))
    with col2:
        avg_age = round(df['age'].mean(), 1)
        st.metric("Average Age", f"{avg_age} yrs")

    # --- Age Distribution Chart ---
    st.markdown("#### 📊 Age Distribution")
    fig1, ax1 = plt.subplots()
    df['age'].value_counts().sort_index().plot(kind='bar', ax=ax1, color='skyblue')
    ax1.set_xlabel("Age")
    ax1.set_ylabel("Count")
    st.pyplot(fig1)

    # --- Entries Over Time Chart ---
    st.markdown("#### 📈 Entries Over Time")
    df_by_date = df.groupby(df['timestamp'].dt.date).size()
    fig2, ax2 = plt.subplots()
    df_by_date.plot(kind='line', marker='o', ax=ax2, color='green')
    ax2.set_xlabel("Date")
    ax2.set_ylabel("Entries")
    st.pyplot(fig2)

    # --- Export to CSV ---
    st.markdown("#### 📤 Export")
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("⬇️ Download CSV", data=csv, file_name="entries.csv", mime="text/csv")

    # --- Full Table View ---
    st.markdown("#### 🗂️ All Entries")
    st.dataframe(df)
else:
    st.info("No entries yet. Please add some data.")
