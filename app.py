import streamlit as st
from style import set_page_config, apply_custom_styles
from database import save_entry, load_entries
import pandas as pd
import matplotlib.pyplot as plt

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

# --- Load data ---
entries = load_entries()
df = pd.DataFrame(entries)

# --- Dashboard ---
if not df.empty:
    st.subheader("📊 Dashboard")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Entries", len(df))

    with col2:
        avg_age = round(df['age'].mean(), 1)
        st.metric("Average Age", f"{avg_age} yrs")

    # Bar chart
    st.markdown("#### Age Distribution")
    fig, ax = plt.subplots()
    df['age'].value_counts().sort_index().plot(kind='bar', ax=ax, color='skyblue')
    ax.set_xlabel("Age")
    ax.set_ylabel("Count")
    st.pyplot(fig)

    # Show full table
    st.markdown("#### 🗂️ All Entries")
    st.dataframe(df)
else:
    st.info("No entries yet. Please add some data.")
