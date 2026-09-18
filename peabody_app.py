import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Peabody Calculator",
    page_icon="logo.png",
    layout="wide"
)

# Define pages
home_page = st.Page(
    "homepage_app.py",
    title="Home",
    icon="💎"
)

vertical_page = st.Page(
    "Vertical_anodes_app.py",
    title="Vertical Anode",
    icon="💎"
)

horizontal_page = st.Page(
    "Horizontal_anodes_app.py",
    title="Horizontal Anode",
    icon="💎"
)

rectifier_page = st.Page(
    "Rectifier_app.py",
    title="Rectifier",
    icon="💎"
)

galvanic_page = st.Page(
    "Galvanicanode_app.py",
    title="Galvanic Anodes",
    icon="💎"
)

current_page = st.Page(
    "Impressedcurrent_app.py",
    title="Impressed Current",
    icon="💎"
)

# Create navigation
pg = st.navigation([
    home_page,
    vertical_page,
    horizontal_page,
    rectifier_page,
    galvanic_page,
    current_page
])

# Run selected page
pg.run()