import streamlit as st
import sys
import os

# --- PATH FIX ---
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

import utils 
import json

# --- FILE LOADING ---
json_path = os.path.join(current_dir, '..', 'content', 'data', '03_gallery_feature.json')

# Load with UTF-8
with open(json_path, 'r', encoding='utf-8') as f:
    galleryfeature_data = json.load(f)

# --- ENGINE LOGIC ---

# 1. UNIQUE KEY for this domain
SESSION_KEY = "galleryfeature_selected_item"

# 2. Initialize
if SESSION_KEY not in st.session_state:
    st.session_state[SESSION_KEY] = None

# 3. Router
if st.session_state[SESSION_KEY]:
    # DETAIL VIEW
    # We must pass 'bomb_data' as the second argument!
    utils.render_detail_view(
        st.session_state[SESSION_KEY], # Arg 1: The ID
        galleryfeature_data,                     # Arg 2: The Data Dictionary <--- THIS WAS MISSING
        session_key=SESSION_KEY        # Arg 3: The Key
    )
else:
    # GRID VIEW (With Hero Mode Active)
    utils.render_grid_view(
        "Featured Gallery", 
        "A collection with a hero section.", 
        galleryfeature_data,
        session_key=SESSION_KEY,
        hero_mode=True 
    )