import streamlit as st
import sympy as sp
from sympy import symbols, Function
import math

st.title("Peabody Design Equations for Vertical Anodes")

#====================
#EQUATION 1
#====================
st.header("Dwight's Equation for Multiple Verticle Anodes in Parallel- Meters")
left, right = st.columns ([2,2])
#INPUT PARAMATERS
with left:
    with st.container(border=True):
        st.subheader("Input Parameters")

        rhov = st.number_input("Soil resistivity in Ωcm", value=4000, key="vertical_multiple_rho")

        Nv = st.number_input("Number of anodes in parallel", value=6, key="vertical_multiple_Nv")

        Lv = st.number_input("Length of anode in meters", value=1.52, key="vertical_multiple_Lv")

        dv = st.number_input("Diameter of anode in meters", value=0.305, key="vertical_multiple_dv")

        Sv = st.number_input("Anode spacing in meters", value=3.05, key="vertical_multiple_Sv")

#DISPLAYING EQUATION
rho, L, d, N, S = sp.symbols('rho L d N S')
with right:
    with st.container(border=True):
        st.latex("Symbols")
        st.latex(f"\\rho =\\text{{Soil resistivity (Ω-cm)}}")
        st.latex(f"{N} = \\text{{Number of anodes}}")
        st.latex(f"{L} = \\text{{Anode length (m)}}")
        st.latex(f"{d} = \\text{{Anode diameter (m)}}")
        st.latex(f"{S} = \\text{{Anode spacing (m)}}")
    with st.container(border=True):
        Rv = ((0.00159*rho)/(N*L)) * ( (sp.log(8*L/d)) -1 + ((2*L/S)*(sp.log(0.656*N))) )
        st.latex(r"R_v = " + sp.latex(Rv))


#CALCULATING RESISTANCE
        R = ((0.00159*rhov)/(Nv*Lv)) * ( (math.log(8*Lv/dv)) -1 + ((2*Lv/Sv)*(math.log(0.656*Nv))) )
        st.latex(f"R_v = {R:.4f}\\ Ω")

#==================
#EQUATION 2
#==================
st.header("")
st.header("Dwight's Equation for Single Vertical Anode Resistance to Earth- Meters")
left, right = st.columns ([2,2])

#INPUT PARAMETERS
with left:
    with st.container(border=True):
        rhovs = st.number_input("Soil resistivity in Ωcm", value=4000, key="vertical_single_rhovs")

        Lvs = st.number_input("Length of anode in meters", value=1.52, key="vertical_single_Lvs")

        dvs = st.number_input("Diameter of anode in meters", value=0.305, key="vertical_single_dvs")

#DISPLAY EQUATION
rho, L, d = sp.symbols('rho L d')
with right:
    with st.container(border=True):
        st.latex("Symbols")
        st.latex(f"\\rho =\\text{{Soil resistivity (Ω-cm)}}")
        st.latex(f"{L} = \\text{{Anode length (m)}}")
        st.latex(f"{d} = \\text{{Anode diameter (m)}}")
    with st.container(border=True):
        Rv = ((0.00159*rho)/L) * ((sp.log(8*L/d)) - 1)
        st.latex(r"R_v = " + sp.latex(Rv))
#CALCULATING RESISTANCE
        R = ((0.00159*rhovs)/Lvs) * ((sp.log(8*Lvs/dvs)) - 1)
        st.latex(f"R_v = {R:.4f}\\ Ω")

#==================
#EQUATION 3
#==================
st.header("")
st.header("Dwight's Equation for Single Vertical Anode Resistance to Earth- Millimeters")
left, right = st.columns ([2,2])

#INPUT PARAMETERS
with left:
    with st.container(border=True):
        rhomm = st.number_input("Soil resistivity in Ωcm", value=5000, key="vertical_single_rhomm")

        Lmm = st.number_input("Length of anode in mm", value=610, key="vertical_single_Lvmm")

        dmm = st.number_input("Diameter of anode in mm", value=178, key="vertical_single_dvmm")

#DISPLAY EQUATION
rho, L, d = sp.symbols('rho L d')
with right:
    with st.container(border=True):
        st.latex("Symbols")
        st.latex(f"\\rho =\\text{{Soil resistivity (Ω-cm)}}")
        st.latex(f"{L} = \\text{{Anode length (mm)}}")
        st.latex(f"{d} = \\text{{Anode diameter (mm)}}")
    with st.container(border=True):
        Rv = (1.59*rho/L) * ((sp.log(8*L/d))-1)
        st.latex(r"R_v = " + sp.latex(Rv))
#CALCULATING RESISTANCE
        R = (1.59*rhomm/Lmm) * ((sp.log(8*Lmm/dmm))-1)
        st.latex(f"R_v = {R:.4f}\\ Ω")
