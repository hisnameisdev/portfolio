import os
import streamlit as st

#Display browser page title
st.set_page_config(
    page_title="Streamlit_CMS_Template",
    layout="wide"
)

#Side menu titles 
pages = {
    "Site Information": [
        st.Page("pages/04_about_contact.py", title="About & Contact [TEMPLATE]"),
        st.Page("pages/profile.py", title="About Me"),
    ],
    "Sections": [
        st.Page("pages/01_gallery01.py", title="Gallery Example 1 [TEMPLATE]"),
        st.Page("pages/02_gallery02.py", title="Gallery Example 2 [TEMPLATE]"),
        st.Page("pages/03_gallery_feature.py", title="Galley w/ Feature [TEMPLATE]"),
        st.Page("pages/project_portfolio.py", title="Active Projects"),
    ],
}
pg = st.navigation(pages)
pg.run()



