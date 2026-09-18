
import streamlit as st

left, right = st.columns([5,1])

with right:
    st.image("logo.png")
with left:
    st.title("Peabody Design Equations Calculator")

st.write("Welcome to the Peabody Engineering Calculator.")

st.divider()

st.subheader("Select a calculation")

st.write("""
Use the navigation menu on the left to select the type of
engineering calculation you want to perform.
""")



#col1, col2, col3 = st.columns(3)

#with col1:
#    with st.container(border=True, ):
#        st.write("**Vertical Anodes**\n\nCalculate resistance for vertical anode systems.")

#with col2:
#    with st.container(border=True):
#        st.write("**Horizontal Anodes**\n\nCalculate resistance for horizontal anode systems.")

#with col3:
#    with st.container(border=True):
#        st.write("**Rectifier**\n\nPerform rectifier sizing and design calculations.")