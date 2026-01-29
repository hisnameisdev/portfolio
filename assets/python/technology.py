import streamlit as st
import json

# Load the data ONCE when the app starts
def load_data():
    with open('assets/json/tech_projects.json', 'r') as f:
        return json.load(f)
# --- DATA STRUCTURE (The "Database") ---
PROJECTS = load_data() 
# Now 'PROJECTS' works exactly like it did before, 
# but the data is safely stored outside the code.

def show_project_detail(project_id):
    """The 'Detail' View: Shows one specific project."""
    data = PROJECTS[project_id]
    
    # Button to go back to the main list
    if st.button("← Back to Mission List"):
        st.session_state.selected_project = None
        st.rerun()
        
    st.title(f"{data['icon']} {data['title']}")
    
    # RENDER DIFFERENT LAYOUTS BASED ON TYPE
    if data['content_type'] == 'manual':
        # The Complex Layout for your Theater Project
        st.info("OPERATOR MANUAL: Audio Engineering Protocol")
        tab1, tab2, tab3 = st.tabs(["Startup Sequence", "Patch List", "Troubleshooting"])
        with tab1:
            st.write("1. Power on the rack...")
        with tab2:
            st.table({"Channel": [1, 2], "Input": ["Mic A", "Mic B"]})
        with tab3:
            st.error("If feedback loop detected: CUT MONITOR BUS.")
            
    else:
        # Standard Layout for simple projects
        st.write(f"**Tags:** {', '.join(data['tags'])}")
        st.write("### Project Brief")
        st.write(data['summary'])
        # You could load a markdown file here: st.markdown(open(f"{project_id}.md").read())

def show_project_grid():
    st.title("Technology Domain", text_alignment="center")
    st.subheader("Active operations, hardware fabrication, and technical documentation.", divider="blue", text_alignment="center")
    
    # 1. Create the 3 Layout Columns
    cols = st.columns(3, gap="medium")
    
    # 2. Convert dictionary to a list so we can index it easily
    # (We need the keys AND values to make the buttons work)
    items = list(PROJECTS.items())

    # 3. The Loop
    for i, (pid, data) in enumerate(items):
        # Math Magic: 
        # If i is 0, it goes to col[0]
        # If i is 1, it goes to col[1]
        # If i is 3, it wraps back to col[0]
        col_index = i % 3 
        
        with cols[col_index]:
            # --- THE CARD DESIGN ---
            # Using a container gives it a nice border box
            with st.container(border=True):
                
                # A. The Image (Stacked on Top)
                # Using a placeholder 'kitten' if no image exists in your data
                img_url = data.get("image", "https://placekitten.com/400/200")
                st.image(img_url, use_container_width=True)
                
                # B. The Title
                st.subheader(f"{data['icon']} {data['title']}")
                
                # C. The Expanding Text (As requested)
                with st.expander("Mission Brief", expanded=False):
                    st.write(data['summary'])
                    # We put the "Tags" inside here to keep the card clean
                    st.caption(f"Tags: {', '.join(data['tags'])}")
                
                # D. The Button
                # We use full width so it looks like a "footer" for the card
                if st.button("Access Terminal", key=pid, use_container_width=True):
                    st.session_state.selected_project = pid
                    st.rerun()

# --- MAIN RENDERER ---
def show():
    # Initialize session state if not present
    if "selected_project" not in st.session_state:
        st.session_state.selected_project = None

    # Router Logic: Show Grid OR Show Detail
    if st.session_state.selected_project:
        show_project_detail(st.session_state.selected_project)
    else:
        show_project_grid()

if __name__ == "__main__":
    show()