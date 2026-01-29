import streamlit as st
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

# --- THE GENERIC DETAIL VIEW ---
import streamlit as st
import os

# --- THE GENERIC DETAIL VIEW ---
# UPDATED: Now accepts 'session_key' with a default value
def render_detail_view(item_id, items_dict, session_key="selected_item"):
    
    data = items_dict.get(item_id)
    if not data:
        st.error("Mission Data Corrupted (Item ID not found).")
        return

    # UPDATED: The Back Button now clears the SPECIFIC key
    if st.button("← Return to Grid", key=f"back_{item_id}"):
        st.session_state[session_key] = None
        st.rerun()

    # ... (The rest of your logic for headers/manual/standard stays the same) ...
    
    # Quick abbreviated version of the rest to keep this snippet readable:
    st.title(f"{data.get('icon', '')} {data.get('title', 'Untitled')}")
    
    c_type = data.get('content_type', 'standard')
    
    if c_type == 'manual':
        # 1. Try to get the config, or use an empty dict if missing
        config = data.get('display_config', {})

        # 2. Get the Banner Text (Default to generic warning if missing)
        banner_text = config.get('banner_text', "⚠️ OPERATIONAL MANUAL")
        banner_type = config.get('banner_type', "info") # info, success, warning, error

        # 3. Dynamic Banner Display
        if banner_type == 'error':
            st.error(banner_text)
        elif banner_type == 'warning':
            st.warning(banner_text)
        else:
            st.info(banner_text)

        # 4. Dynamic Tabs
        # Default to "Field Guide" and "Specs" if not specified
        tab_names = config.get('tabs', ["Field Guide", "Specs"])
        
        # Unpack the tabs dynamically
        # (This is a bit tricky in Streamlit, but here is the safe way)
        tabs = st.tabs(tab_names)
        
        # Tab 1 Content (Always the Markdown)
        with tabs[0]:
            # THE FLEXIBLE PART (The Painting)
            # We just load the markdown and let it render however it wants.
            
            # If functions.py is inside /assets/python/
            md_path = os.path.join(current_dir, "..", "..", "assets", "content", data['markdown_file'])
            
            with open(md_path, 'r', encoding='utf-8') as f:
                content = f.read()
                st.markdown(content) # <--- This renders the lists, tables, and code blocks
        
    else:
        # --- STANDARD VIEW (Bulletproof Edition) ---
        
        # 1. Image Logic
        # Try to find an image key at the root
        image_name = data.get('image')
        
        if image_name:
            # Check if it's a web URL (starts with http)
            if image_name.startswith("http"):
                st.image(image_name)
            else:
                # It's a local file. We need to find it.
                # Assuming images live in /assets/images/
                # We reuse the 'current_dir' logic you used for markdown
                image_path = os.path.join(current_dir, "..", "..", "assets", "images", image_name)
                
                # Only try to show it if the file actually exists
                if os.path.exists(image_path):
                    st.image(image_path)
                else:
                    # Optional: Print a warning to console (not the user)
                    print(f"Warning: Could not find image at {image_path}")

        # 2. Text Logic
        st.write("### Overview")
        
        # Use .get() with a default string so it never crashes
        summary_text = data.get('summary', "No mission brief available.")
        st.write(summary_text)
        
        # 3. Optional: Render 'Tags' if they exist
        tags = data.get('tags', [])
        if tags:
            st.caption(f"Tags: {', '.join(tags)}")

# --- THE GENERIC GRID VIEW ---
# UPDATED: Now accepts 'session_key'
def render_grid_view(page_title, page_description, items_dict, session_key="selected_item", hero_mode=False):
    
    st.title(page_title)
    st.write(page_description)
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Convert dictionary to list of items
    items = list(items_dict.items())
    
    # --- HERO SECTION LOGIC ---
    if hero_mode and len(items) > 0:
        # 1. Peel off the first item (The "Latest")
        hero_pid, hero_data = items[0]
        
        # 2. Remove it from the list so it doesn't show up twice
        items = items[1:] 
        
        # 3. Render the Hero Card (Full Width)
        st.write("### 🌟 Latest Entry")
        with st.container(border=True):
            # Two columns: Image on Left, Text on Right (looks premium)
            hc1, hc2 = st.columns([1, 2])
            
            with hc1:
                # Same image logic as before
                h_img = hero_data.get("image")
                if h_img and not h_img.startswith("http"):
                     h_img = os.path.join(current_dir, "..", "..", "assets", "images", h_img)
                
                # Default to kitten if missing
                st.image(h_img or "https://placekitten.com/600/400", use_container_width=True)
            
            with hc2:
                st.subheader(f"{hero_data.get('icon', '')} {hero_data.get('title', 'Untitled')}")
                st.write(hero_data.get('summary', ''))
                st.write("") # Spacer
                if st.button("Read Feature", key=f"hero_{hero_pid}"):
                    st.session_state[session_key] = hero_pid
                    st.rerun()
        
        st.divider() # A nice line to separate Hero from the rest

    # --- STANDARD GRID LOGIC (The Rest of the Items) ---
    cols = st.columns(3, gap="medium")
    
    for i, (pid, data) in enumerate(items):
        col_index = i % 3 
        with cols[col_index]:
            with st.container(border=True):
                # ... (The rest of your existing grid code goes here) ...
                # ... (Copy the exact image/text/button logic you already have) ...
                
                # Abbreviated for clarity:
                img = data.get("image", "https://placekitten.com/400/200")
                if img and not img.startswith("http"):
                    img = os.path.join(current_dir, "..", "..", "assets", "images", img)
                st.image(img, use_container_width=True)
                
                st.subheader(f"{data.get('icon', '')} {data.get('title')}")
                with st.expander("Brief"):
                    st.write(data.get('summary'))
                
                if st.button("Open", key=f"btn_{pid}", use_container_width=True):
                    st.session_state[session_key] = pid
                    st.rerun()