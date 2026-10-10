import streamlit as st
st.set_page_config(page_title="The Frictionless Learning Paradox", page_icon="🧠")
st.title("🧠 The Frictionless Learning Paradox")
st.subheader("Smart Speed Bump AI: Balancing AI Assistance with Productive Struggle")
student_query = st.text_area("Ask your AI tutor a question:")
if st.button("Submit to Tutor"):
    if "code" in student_query.lower():
        st.error("⚠️ Low-Friction Warning Triggered! The Socratic Brake is active.")
    else:
        st.success("✨ Good effort detected! Here is your guidance.")
