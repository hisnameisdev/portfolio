import streamlit as st
import os


st.title("About the System")

# --- PROFILE SECTION ---
col1, col2 = st.columns([1, 2], gap="medium")

with col1:
    # Placeholder for a profile picture
    # Ideally, put a file named 'profile.jpg' in content/images/
    st.image("https://placekitten.com/300/300", caption="The System", use_container_width=True)

with col2:
    st.write("""
    ### Hello there! 👋
    
    This is a template bio. You should replace this text with your actual background. 
    
    **Focus on:**
    * Your primary discipline (e.g., "Systems Engineer").
    * Your philosophical approach (e.g., "Function over form").
    * What you are currently building.
    """)
    
    st.info("💡 **Pro Tip:** Edit `pages/04_about_contact.py` to change this text.")

st.divider()

# --- CONTACT SECTION ---
st.subheader("📬 Get in touch")

contact_form = """
<form action="https://formsubmit.co/YOUR_EMAIL_HERE" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required style="width: 100%; padding: 8px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 4px;">
     <input type="email" name="email" placeholder="Your Email" required style="width: 100%; padding: 8px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 4px;">
     <textarea name="message" placeholder="Transmission Content" required style="width: 100%; padding: 8px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 4px; min-height: 100px;"></textarea>
     <button type="submit" style="background-color: #ff4b4b; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer;">Send Transmission</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

st.caption("Note: Update the email address in the form HTML code inside `pages/04_about_contact.py` to make this functional.")