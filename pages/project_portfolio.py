import streamlit as st
import sys
import os

# --- THE FIX: ADD CURRENT FOLDER TO SYSTEM PATH ---
current_dir = os.path.dirname(os.path.abspath(__file__))

if current_dir not in sys.path:
    sys.path.append(current_dir)

import utils 
import json

# --- FILE LOADING ---
# (This part stays exactly the same)
json_path = os.path.join(current_dir, '..', 'content', 'data', 'project_portfolio.json')

with open(json_path, 'r', encoding='utf-8') as f:
    portfolio_data = json.load(f)

# --- ENGINE LOGIC (THE NEW REPLACEMENT PART) ---

# 1. Define the unique key for this specific page
# (For Mind & Body, you will change this to "mind_selected_item")
SESSION_KEY = "portfolio_selected_item"

# 2. Initialize it if it doesn't exist
if SESSION_KEY not in st.session_state:
    st.session_state[SESSION_KEY] = None

# 3. The Router (Check specific key, not generic key)
if st.session_state[SESSION_KEY]:
    # RENDER DETAIL
    utils.render_detail_view(
        st.session_state[SESSION_KEY], 
        portfolio_data, 
        session_key=SESSION_KEY  # <--- Critical: Tell the Back button which key to wipe
    )
else:
    # RENDER GRID
    utils.render_grid_view(
        "Active Projects", 
        "A place for everything, and everything in its place. Select a project below to find out more about it", 
        portfolio_data,
        session_key=SESSION_KEY  # <--- Critical: Tell the Open button which key to set
    )