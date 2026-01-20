import streamlit as st

# --- PAGE SETUP ---
# This must be the first command in your app
st.set_page_config(
    page_title="Home",
    page_icon="👋",
)

# --- SIDEBAR ---
# This adds a persistent note to the sidebar
st.sidebar.info("Select a project above to view documentation.")

# --- MAIN CONTENT ---
st.title("Hi, I'm [Your Name] 👋")
st.subheader("IT Specialist | Robotics Student | Maker")

st.markdown("""
### 🚀 About Me
I am an IT professional transitioning into **Robotics and Integrated Technologies**. 
This portfolio documents my journey through technical projects, from soldering logic gates to designing systems in CAD.

**Current Focus:**
* 🎓 **Study:** Cert IV in Integrated Technologies (Robotics Control Systems)
* 🛠️ **Projects:** Electronics, 3D Printing, Python Automation
* 🧠 **Goal:** Solving problems through systems thinking.

---

### 📂 How to navigate this site
Use the sidebar on the left to view documentation for specific projects.
* **Build Notes:** How I built this portfolio using Python & Streamlit.
* **Coming Soon:** Logic Gates & 3D Printed Modular Furniture.
""")

# --- FOOTER ---
st.divider()
st.caption("Built with ❤️ using Python & Streamlit")