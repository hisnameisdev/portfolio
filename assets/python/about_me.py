import streamlit as st
import time

def show():
    st.title("System Profile: Devon Wright")

    # --- TOP SECTION: THE SPLIT ---
    # We use a [1, 2] ratio so the text is wider than the photo
    col1, col2 = st.columns([1, 2], gap="medium")

    with col1:
        #Profile image
        st.image("assets/images/beholder.jpg", caption="Operator Avatar", use_container_width=True)
        
        
    with col2:
        st.subheader("System Overview")
        st.write("""
        **Status:** Currently Unallocated  
        **Role:** Technical Consultant & Proxy Device Operative  
        
        Hello! I navigate the weird intersection between hardware, software, and the 
        people who break them. I specialize in turning coffee into code and 
        complex systems into understandable metaphors.
        
        Currently exploring the boundaries of Streamlit, 3D printing, and 
        generative AI.
        """)
        
        # ODD COMPONENT 2: The "Expander" for deep dives
        # This keeps the page clean but lets people dig if they want.
        with st.expander("Read My Philosophy on Technology"):
            st.write("""
            Knowledge can never be complete. Relentlessly pursuing it 
            will not be the way. Instead, I focus on building adaptable 
            frameworks for understanding...
            """)

    st.divider()

    # --- ODD COMPONENT 3: "LIVE" METRICS ---
    # A dashboard that visualizes your current "state"
    st.subheader("Current Operating Parameters")
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Caffeine Level", "85%", "15%")
    m2.metric("Procrastination", "High", "Critical")
    m3.metric("Ideas Pending", "42", "-3")
    m4.metric("3D Printer", "Idle", "Ready")

    # --- ODD COMPONENT 4: THE SKILL SLIDERS ---
    # Instead of a static list, let the user "audit" your skills
    st.subheader("Skill Calibration")
    st.caption("Adjust sliders to view confidence intervals.")
    
    st.slider("Python Logic", 0, 100, 80)
    st.slider("UI Design", 0, 100, 40)
    st.slider("Philosophy / Ethics", 0, 100, 95)

# If running this file directly (not via main.py), show it
if __name__ == "__main__":
    show()