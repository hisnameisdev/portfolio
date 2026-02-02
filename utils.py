import streamlit as st
import os

# --- THE GENERIC DETAIL VIEW ---
def render_detail_view(item_id, items_dict, session_key="selected_item"):
    
    # 1. Get the Data
    data = items_dict.get(item_id)
    if not data:
        st.error("Content not found.")
        return

    # 2. The Back Button (Clears the specific session key)
    if st.button("← Return", key=f"back_{item_id}"):
        st.session_state[session_key] = None
        st.rerun()

    # 3. Title & Icon
    st.title(f"{data.get('icon', '')} {data.get('title', 'Untitled')}")

    # 4. Content Logic
    c_type = data.get('content_type', 'standard')
    current_dir = os.path.dirname(os.path.abspath(__file__))

    if c_type == 'manual':
        # --- MANUAL MODE (Tabs & Markdown) ---
        config = data.get('display_config', {})
        
        # Banner Logic
        banner_text = config.get('banner_text')
        if banner_text:
            b_type = config.get('banner_type', 'info')
            if b_type == 'error': st.error(banner_text)
            elif b_type == 'warning': st.warning(banner_text)
            else: st.info(banner_text)

        # Tabs Logic
        # 1. Get the list of tab configurations (could be strings OR dicts)
        tab_configs = config.get('tabs', ["Documentation"]) 

        if tab_configs:
            # 2. Extract Names safely
            tab_names = []
            for t in tab_configs:
                if isinstance(t, str):
                    tab_names.append(t)  # It's just a string like "The Guide"
                elif isinstance(t, dict):
                    tab_names.append(t.get("name", "Tab")) # It's a config object
            
            # 3. Create Tabs
            created_tabs = st.tabs(tab_names)

            # 4. The Smart Loop
            for i, t in enumerate(tab_configs):
                with created_tabs[i]:
                    
                    # --- HANDLE OLD FORMAT (String) ---
                    if isinstance(t, str):
                        # Default behavior: Look for 'markdown_file' at the root
                        md_file = data.get('markdown_file')
                        if i == 0 and md_file: # Only put main doc in the first tab
                            md_path = os.path.join(current_dir, "content", "documents", md_file)
                            if os.path.exists(md_path):
                                with open(md_path, 'r', encoding='utf-8') as f:
                                    st.markdown(f.read())
                            else:
                                st.warning(f"File not found: {md_file}")
                        else:
                            st.info(f"{t} content placeholder")

                    # --- HANDLE NEW FORMAT (Dictionary) ---
                    elif isinstance(t, dict):
                        file_name = t.get("file")
                        file_type = t.get("type", "markdown")
                        
                        if file_type == "markdown" and file_name:
                            path = os.path.join(current_dir, "content", "documents", file_name)
                            if os.path.exists(path):
                                with open(path, 'r', encoding='utf-8') as f:
                                    st.markdown(f.read())
                            else:
                                st.error(f"Missing doc: {file_name}")
                        # Add other types (image/json) here if needed


# --- THE GENERIC GRID VIEW ---
def render_grid_view(page_title, page_description, items_dict, session_key="selected_item", hero_mode=False):
    
    st.title(page_title)
    st.write(page_description)
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    items = list(items_dict.items())
    
    # --- HERO SECTION (Optional) ---
    if hero_mode and len(items) > 0:
        hero_pid, hero_data = items[0]
        items = items[1:] # Remove hero from grid list
        
        st.write("### 🌟 Featured")
        with st.container(border=True):
            c1, c2 = st.columns([1, 2])
            with c1:
                # Hero Image
                h_img = hero_data.get("image")
                if h_img and not h_img.startswith("http"):
                     # UPDATED PATH
                     h_path = os.path.join(current_dir, "content", "images", h_img)
                     if os.path.exists(h_path): h_img = h_path
                st.image(h_img or "https://placekitten.com/600/400", use_container_width=True)
            
            with c2:
                st.subheader(f"{hero_data.get('icon', '')} {hero_data.get('title')}")
                st.write(hero_data.get('summary'))
                if st.button("Read Feature", key=f"hero_{hero_pid}"):
                    st.session_state[session_key] = hero_pid
                    st.rerun()
        st.divider()

    # --- STANDARD GRID ---
    cols = st.columns(3, gap="medium")
    
    for i, (pid, data) in enumerate(items):
        with cols[i % 3]:
            with st.container(border=True):
                # Card Image
                img = data.get("image")
                final_img = "https://placekitten.com/400/200" # Fallback
                
                if img:
                    if img.startswith("http"):
                        final_img = img
                    else:
                        # UPDATED PATH
                        loc_path = os.path.join(current_dir, "content", "images", img)
                        if os.path.exists(loc_path): final_img = loc_path
                
                st.image(final_img, use_container_width=True)
                
                st.subheader(f"{data.get('icon', '')} {data.get('title')}")
                
                with st.expander("Summary"):
                    st.write(data.get('summary'))
                
                if st.button("Open", key=f"btn_{pid}", use_container_width=True):
                    st.session_state[session_key] = pid
                    st.rerun()