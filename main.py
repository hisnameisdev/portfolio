import streamlit as st

st.set_page_config(
    page_title="Wright On",
    layout="wide"  # <--- This is the magic switch
)

pages = {
    "The Creator": [
        st.Page("assets/python/about_me.py", title="About Me"),
        st.Page("assets/python/contact.py", title="Contact"),
    ],
    "Domains": [
        st.Page("assets/python/technology.py", title="Technology"),
        st.Page("assets/python/mind_and_body.py", title="Mind & Body"),
        st.Page("assets/python/pipebombs.py", title="Pipebombs"),
    ],
}
pg = st.navigation(pages)
pg.run()



