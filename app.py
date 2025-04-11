import streamlit as st
from style import set_page_config, apply_custom_styles
from database import save_entry, load_entries, update_entry, delete_entry
import pandas as pd
import matplotlib.pyplot as plt

# --- Theme Toggle ---
theme_choice = st.sidebar.selectbox("🎨 Theme", ["light", "dark", "blue"])
set_page_config()
apply_custom_styles(theme_choice)

st.title("📝 Simple Data Entry App")

# --- Form to Add New Entry ---
with st.form("entry_form"):
    st.subheader("➕ Add New Entry")
    name = st.text_input("Name")
    email = st.text_input("Email")
    age = st.number_input("Age", min_value=0, max_value=120)
    notes = st.text_area("Notes")
    submitted = st.form_submit_button("Save Entry")

    if submitted:
        save_entry(name, email, age, notes)
        st.success("✅ Entry saved successfully!")
        st.experimental_rerun()

# --- Load & Prepare Data ---
entries = load_entries()
df = pd.DataFrame(entries)

if not df.empty:
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # --- Search & Filter ---
    st.subheader("🔍 Filter Entries")
    search_query = st.text_input("Search by name or email")
    if search_query:
        df = df[df['name'].str.contains(search_query, case=False) | df['email'].str.contains(search_query, case=False)]

    # --- Dashboard Stats ---
    st.subheader("📊 Dashboard")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Entries", len(df))
    with col2:
        avg_age = round(df['age'].mean(), 1)
        st.metric("Average Age", f"{avg_age} yrs")

    # --- Charts ---
    st.markdown("#### 📊 Age Distribution")
    fig1, ax1 = plt.subplots()
    df['age'].value_counts().sort_index().plot(kind='bar', ax=ax1, color='skyblue')
    ax1.set_xlabel("Age")
    ax1.set_ylabel("Count")
    st.pyplot(fig1)

    st.markdown("#### 📈 Entries Over Time")
    df_by_date = df.groupby(df['timestamp'].dt.date).size()
    fig2, ax2 = plt.subplots()
    df_by_date.plot(kind='line', marker='o', ax=ax2, color='green')
    ax2.set_xlabel("Date")
    ax2.set_ylabel("Entries")
    st.pyplot(fig2)

    # --- Export to CSV ---
    st.subheader("📤 Export")
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("⬇️ Download CSV", data=csv, file_name="entries.csv", mime="text/csv")

    # --- Edit or Delete Entries ---
    st.subheader("🛠️ Edit or Delete Entries")
    for idx, row in df.iterrows():
        with st.expander(f"{row['name']} ({row['email']})"):
            new_name = st.text_input("Edit Name", row['name'], key=f"name_{idx}")
            new_email = st.text_input("Edit Email", row['email'], key=f"email_{idx}")
            new_age = st.number_input("Edit Age", value=row['age'], min_value=0, max_value=120, key=f"age_{idx}")
            new_notes = st.text_area("Edit Notes", row['notes'], key=f"notes_{idx}")

            col1, col2 = st.columns([1, 1])
            with col1:
                if st.button("💾 Save Changes", key=f"save_{idx}"):
                    update_entry(idx, new_name, new_email, new_age, new_notes)
                    st.success("✅ Entry updated!")
                    st.experimental_rerun()
            with col2:
                if st.button("🗑️ Delete", key=f"delete_{idx}"):
                    delete_entry(idx)
                    st.warning("🗑️ Entry deleted.")
                    st.experimental_rerun()

    # --- Table of Entries ---
    st.subheader("📋 All Entries")
    st.dataframe(df)

else:
    st.info("No entries yet. Please add some data to get started.")
