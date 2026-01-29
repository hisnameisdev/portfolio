import streamlit as st

def show():
    st.title("Contact the Operative")

    st.write("Broadcast a signal into the void. If the frequencies align, I will respond.")

    # --- THE FORM CONTAINER ---
    # clear_on_submit=True wipes the text boxes after they hit Send
    with st.form(key="contact_form", clear_on_submit=True):
        
        # Two columns for Name and Email so it looks compact
        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("Entity Name")
        with c2:
            email = st.text_input("Return Frequency (Email)")
        
        # The Type of Inquiry (Selectbox)
        inquiry_type = st.selectbox(
            "Nature of Inquiry",
            ["General Query", "Project Proposal", "Existential Crisis Support", "Report a Glitch"]
        )
        
        # The Message Body
        message = st.text_area("Transmission Content", height=150)

        # The Submit Button
        # This is special: It must be INSIDE the 'with st.form' block.
        submit_button = st.form_submit_button(label="Transmit Signal")

    # --- LOGIC AFTER SUBMISSION ---
    if submit_button:
        # Check if they actually typed anything
        if not name or not email:
            st.error("Error: Transmission incomplete. Identity parameters required.")
        else:
            # THIS IS WHERE THE MAGIC WOULD HAPPEN
            # For now, we simulate a successful transmission.
            
            st.success("Signal Received. Acknowledgment protocol initiated.")
            
            # Optional: Show them what they sent (Debug mode)
            with st.expander("View Transmission Packet Log"):
                st.json({
                    "name": name,
                    "email": email,
                    "type": inquiry_type,
                    "message": message
                })

if __name__ == "__main__":
    show()