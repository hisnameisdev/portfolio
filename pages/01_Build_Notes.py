import streamlit as st

st.title("Project 1: Building this Portfolio")

st.markdown("""
### The Goal
To create a low-maintenance, publicly accessible portfolio to document my learning in coding, electronics, and 3D printing.

### The Stack
* **Python & Streamlit:** For the frontend and logic.
* **VS Code:** For development.
* **GitHub:** For version control.
* **Streamlit Community Cloud:** For hosting (CI/CD).
""")

st.subheader("Why this approach?")
st.write("""
I chose Streamlit because it allows me to focus on *content* and *logic* rather than HTML/CSS. 
It deploys directly from GitHub, meaning I don't have to manage a server or FTP files. 
This reduces the friction of adding new projects, helping me avoid 'setup fatigue.'
""")

st.subheader("The 'Hello World' Code")
st.code("""
import streamlit as st

st.title("My Technical Portfolio")
st.write("Current Status: Building resilience and shipping code.")
st.write("---")
st.write("Hello, World! This site is live.")
""", language="python")

st.success("Status: COMPLETED. This site is live and self-documenting.")