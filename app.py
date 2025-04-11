import streamlit as st
from style import set_page_config, apply_custom_styles
from database import save_entry, load_entries

set_page_config()
apply_custom_styles()

st.title("📝 Simple Data Entry App")

with st.form("entry_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    age = st.number_input("Age", min_value=0, max_value=120)
    notes = st.text_area("Notes")
    submitted = st.form_submit_button("Save Entry")

    if submitted:
        save_entry(name, email, age, notes)
        st.success("✅ Entry saved successfully!")

st.subheader("📋 Previous Entries")
entries = load_entries()
for entry in entries:
    st.markdown(f"- **{entry['name']}** ({entry['email']}), Age: {entry['age']} — {entry['notes']}")
