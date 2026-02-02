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
        st.Page("pages/04_about_contact.py", title="About & Contact"),
    ],
    "Sections": [
        st.Page("pages/01_gallery01.py", title="Gallery Example 1"),
        st.Page("pages/02_gallery02.py", title="Gallery Example 2"),
        st.Page("pages/03_gallery_feature.py", title="Galley w/ Feature"),
    ],
}
pg = st.navigation(pages)
pg.run()



