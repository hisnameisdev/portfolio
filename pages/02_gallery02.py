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
# Ensure you have 'assets/json/mind_body.json' created!
json_path = os.path.join(current_dir, '..', 'content', 'data', '02_gallery02.json')

# Load with UTF-8 to handle emojis like 🧘
with open(json_path, 'r', encoding='utf-8') as f:
    gallery02_data = json.load(f)

# --- ENGINE LOGIC ---

# 1. UNIQUE KEY for this domain
SESSION_KEY = "gallery02_selected_item"

# 2. Initialize
if SESSION_KEY not in st.session_state:
    st.session_state[SESSION_KEY] = None

# 3. Router
if st.session_state[SESSION_KEY]:
    utils.render_detail_view(
        st.session_state[SESSION_KEY], 
        gallery02_data, 
        session_key=SESSION_KEY # Pass the unique key
    )
else:
    utils.render_grid_view(
        "Gallery 02", 
        "A generic tiled gallery to display items", 
        gallery02_data,
        session_key=SESSION_KEY # Pass the unique key
    )