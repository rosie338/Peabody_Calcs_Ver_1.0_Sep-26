import streamlit as st
import sympy as sp
from sympy import symbols, Function
import math

st.title("Peabody Design Equations for Horizontal Anodes")

#====================
#EQUATION 1
#====================
st.header("Dwight's Equation for Multiple Anodes Installed Horizontally- Meters")
left, right = st.columns ([2,2])
#INPUT PARAMATERS
with left:
    with st.container(border=True):
        st.subheader("Input Parameters")

        rhoh = st.number_input("Resistivity of backfill material (or earth) in Ωcm", value=10000, key="horizontal_multiple_rho")

        Lh = st.number_input("Length of anode in meters", value=4, key="horizontal_multiple_Lv")

        dh = st.number_input("Diameter of anode in meters", value=0.3, key="horizontal_multiple_dv")

        Sh = st.number_input("Twice Depth of Anode in meters", value=3, key="horizontal_multiple_Sv")

#DISPLAYING EQUATION
rho, L, d, S = sp.symbols('rho L d S')
with right:
    with st.container(border=True):
        st.latex("Symbols")
        st.latex(f"\\rho =\\text{{Backfill material resistivity (Ωcm)}}")
        st.latex(f"{L} = \\text{{Anode length (m)}}")
        st.latex(f"{d} = \\text{{Anode diameter (m)}}")
        st.latex(f"{S} = \\text{{Twice Anode Depth (m)}}")
    with st.container(border=True):
        Rv = ((0.00159*rho)/(L)) * ( sp.log((( (4*L**2) + (4*L*sp.sqrt ( (S**2) + (L**2) ) ))/(d*S))) + (S/L) - ((sp.sqrt((S**2) + (L**2)))/L) - 1)
        st.latex(r"R_v = " + sp.latex(Rv))
#CALCULATING RESISTANCE
        R = ((0.00159*rhoh)/(Lh)) * ( sp.log((( (4*Lh**2) + (4*Lh*sp.sqrt ( (Sh**2) + (Lh**2) ) ))/(dh*Sh))) + (Sh/Lh) - ((sp.sqrt((Sh**2) + (Lh**2)))/Lh) - 1)
        st.latex(f"R_v = {R:.4f}\\ Ω")


