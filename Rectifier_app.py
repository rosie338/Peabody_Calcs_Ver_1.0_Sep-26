import streamlit as st
import sympy as sp
from sympy import symbols, Function
import math

#====================
#EQUATION 1
#====================
st.title("Peabody Rectifier Calculations")
st.header("Rectifier Total Circuit Resistance")
left, right = st.columns ([2,2])
#INPUT PARAMATERS
with left:
    with st.container(border=True):
        st.subheader("Input Parameters")

        R_Gbedh = st.number_input("Groundbed resistance in Ω", value=0.03, key="groundbed_res")

        R_Ch = st.number_input("Cable Resistance in Ω", value=0.097, key="cable_res")

        R_Sh = st.number_input("Pipeline/Structure to Earth Resistance in Ω", value=7.53, key="pipe/struc_to_ground_res")


#DISPLAYING EQUATION
R_Gbed, R_C, R_S = sp.symbols('R_Gbed R_C R_S')
with right:
    with st.container(border=True):
        st.latex("Symbols")
        st.latex(f"R_Gbed =\\text{{Groundbed resistance (Ω))}}")
        st.latex(f"{R_C} = \\text{{Cable Resistance (Ω)}}")
        st.latex(f"{R_S} = \\text{{Pipeline/structure to Earth Resistance (Ω)}}")
    with st.container(border=True):
        R_T = R_Gbed + R_C + R_S
        st.latex(r"R_T = " + sp.latex(R_T))
#CALCULATING RESISTANCE
        R = R_Gbedh + R_Ch + R_Sh
        st.latex(f"R_T = {R:.4f}\\ Ω")



#=====================
#EQUATION 2
#=====================
st.header("Deep Anode Ground Bed Resistance- meters")
left, right = st.columns([2,2])
#INPUT PARAMETERS
with left:
    with st.container(border=True):
        st.subheader("Input Parameters")
        rhor = st.number_input("Effective Soil Resistivity in Ωcm", value=10000, format="%.3f", key="effectivesoilres")
        Lr = st.number_input("Anode Length in meters", value=12, format="%.3f",key="anodelengthr")
        dr = st.number_input("Anode Diameter in meters", value=0.203, format="%.3f", key="anodediameterr")

rho, L, d = sp.symbols('rho L d')
with right:
    with st.container(border=True):
        st.latex("Symbols")
        st.latex(f"\\rho =\\text{{Effective Soil resistivity (Ωcm)}}")
        st.latex(f"{L} = \\text{{Anode length (m)}}")
        st.latex(f"{d} = \\text{{Anode diameter (m)}}")
    with st.container(border=True):
        Rv = ((0.00159*rho)/L)*((sp.log((8*L)/d))-1)
        st.latex(r"R_v = " + sp.latex(Rv))

        R = ((0.001591*rhor)/Lr)*((sp.log((8*Lr)/dr))-1)
        st.latex(f"R_v = {R:.4f}\\ Ω")

#=====================
#EQUATION 3
#=====================
st.header("Rectifier Efficiency")
left, right = st.columns([2,2])
with left:
    with st.container(border=True):
        st.subheader("Input Parameters")
        Ke = st.number_input("Meter Constant", value=0.005, key="meter_constant")
        Ne = st.number_input("Number of Disk Revolutions", value=4, key="noofrevs")
        Te = st.number_input("Time in Seconds", value=10, format="%.3f", key="time")
        DC_Voltse = st.number_input("DC Volts (V)", value = 48.00, key="DCVOLTS")
        DC_Ampse = st.number_input("DC_Amps (A)", value=50.00, key="DCAMPS")

#PRINTING EQUATIONS AND SYMBOLS
K, N, T, DC_Volts, DC_Amps, DC_OutputPower, AC_InputPower = sp.symbols('K N T DC_Volts DC_Amps DC_OutputPower AC_InputPower')
with right:
    with st.container(border=True):
        st.latex("Symbols")
        st.latex(f"{K} =\\text{{Meter Constant}}")
        st.latex(f"{N} = \\text{{Number of Disk Revolutions}}")
        st.latex(f"{T} = \\text{{Time in Seconds}}")
    with st.container(border=True):
        AC_Input_Power = (3600*K*N)/T
        DC_Output_Power = DC_Volts * DC_Amps

        st.latex(r"\text{AC Input Power} = " + sp.latex(AC_Input_Power))
        st.latex(r"\text{DC Input Power} = " + sp.latex(DC_Output_Power))
        st.latex(
    r"\text{Efficiency} = "
    r"\frac{\text{DC Output Power}}{\text{AC Input Power}}"
    r"\times 100"
)

#CALCULATING EFFICIENCY
        AC_Input_Powere = (3600*Ke*Ne)/Te
        DC_Output_Powere = DC_Voltse * DC_Ampse
        Efficiency = (DC_Output_Powere/AC_Input_Powere)*100

        st.latex(f"\\text{{AC Input Power}} = {float(AC_Input_Powere):.2f}")
        st.latex(f"\\text{{DC Output Power}} = {float(DC_Output_Powere):.2f}")
        st.latex(f"\\text{{Efficiency}} = {float(Efficiency):.2f}\\%")
    




