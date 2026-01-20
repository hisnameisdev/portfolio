import streamlit as st

st.set_page_config(page_title="Build Notes", page_icon="📝")

st.markdown("# 📝 Project 1: The Portfolio Itself")
st.sidebar.header("Project 1: Portfolio")

# 1. The Challenge (Why did you do this?)
st.markdown("""
### 🎯 The Challenge
I needed a way to document my work in electronics and coding without falling into the trap of "maintenance fatigue." 
Traditional website builders (Wix, etc.) felt too restrictive, but self-hosting a server was too much friction.

**Requirements:**
* **Low Maintenance:** No server management or security patches.
* **Code-First:** The site itself should demonstrate technical competence.
* **Free/Low Cost:** No monthly fees for basic hosting.
""")

st.divider()

# 2. The Solution (How did you solve it?)
st.markdown("### 🛠️ The Tech Stack")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Language", value="Python 3.10")
with col2:
    st.metric(label="Framework", value="Streamlit")
with col3:
    st.metric(label="Hosting", value="Community Cloud")

st.markdown("""
I chose **Streamlit** because it allows me to write frontend interfaces entirely in Python. 
This removes the need for HTML/CSS/JS context switching.
""")

# 3. Technical Implementation (The "Meat")
with st.expander("See the Source Code Structure"):
    st.code("""
    portfolio/
    ├── Home.py              # The Main Bio Page
    ├── pages/               # Automatic Navigation Menu
    │   ├── 01_Build_Notes.py
    │   └── 02_Logic_Gates.py (Coming Soon)
    └── requirements.txt     # Dependencies
    """, language="text")

st.info("💡 **Lesson Learned:** Using Streamlit's native `pages/` folder automates the navigation menu, saving hours of UI work.")

st.divider()

# 4. Future Roadmap
st.markdown("### 🔮 What's Next?")
st.checkbox("Deploy the 'Hello World' version", value=True, disabled=True)
st.checkbox("Customize the 'Home' page bio", value=True, disabled=True)
st.checkbox("Document the 'Logic Gates' project", value=False)