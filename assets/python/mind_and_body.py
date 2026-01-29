import streamlit as st
import sys
import os

# --- PATH FIX ---
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

import functions 
import json

# --- FILE LOADING ---
# Ensure you have 'assets/json/mind_body.json' created!
json_path = os.path.join(current_dir, '..', 'json', 'mindbody_projects.json')

# Load with UTF-8 to handle emojis like 🧘
with open(json_path, 'r', encoding='utf-8') as f:
    mind_data = json.load(f)

# --- ENGINE LOGIC ---

# 1. UNIQUE KEY for this domain
SESSION_KEY = "mind_selected_item"

# 2. Initialize
if SESSION_KEY not in st.session_state:
    st.session_state[SESSION_KEY] = None

# 3. Router
if st.session_state[SESSION_KEY]:
    functions.render_detail_view(
        st.session_state[SESSION_KEY], 
        mind_data, 
        session_key=SESSION_KEY # Pass the unique key
    )
else:
    functions.render_grid_view(
        "Mind & Body", 
        "Physical training and philosophical frameworks.", 
        mind_data,
        session_key=SESSION_KEY # Pass the unique key
    )