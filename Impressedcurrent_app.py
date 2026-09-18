import streamlit as st
import sympy as sp
from sympy import symbols, Function
import math

st.title("Peabody Design Equations for Impressed Current")

#====================
#EQUATION 1
#====================
st.header("Impressed Current- Number of Anodes Required")
left, right = st.columns ([2,2])
#INPUT PARAMATERS
with left:
    with st.container(border=True):
        st.subheader("Input Parameters")

        Wt = st.number_input("Weight per Anode (Kg)", value=27.2, key="weight")

        CR = st.number_input("Consumption Rate (Kg/Amp.year)", value=0.34, key="consumptionrate")

        DL = st.number_input("Desired Lide (years)", value=20, key="desired life")

        Current = st.number_input("Current Required (Amps)", value=3, key="Currentrequired")

        UF = st.number_input("Utilisation Factor", value=0.6, key="utilisationfactor")

with right:
    with st.container(border=True):
        st.latex(
            r"\text{Number of Anodes} = "
            r"\frac{\text{Consumption Rate x Desired Life x Current Required}}{\text{Utilisation Factor x Weight per Anode}}")

        number = sp.ceiling((CR * DL * Current)/(UF * Wt))
        st.latex(f"\\text{{Number of Anodes}} = {float(number)}")


#==================
#EQUATION 2
#==================
st.header("")
st.header("Number of Anodes Required Based on Current Discharge")
left, right = st.columns ([2,2])
#INPUT PARAMATERS
with left:
    with st.container(border=True):
        st.subheader("Input Parameters")

        Current = st.number_input("Current Required (Amps)", value=3, key="requiredcurrent")

        MD = st.number_input("Maximum Discharge Per Anode (Amps)", value=0.6, key="maxdischarge")

with right:
    with st.container(border=True):
        st.latex(
         r"\text{Number of Anodes} = "
         r"\frac{\text{Current Required}}{\text{Maximum Discharge*}}")

        number_maxdis = sp.ceiling((Current/MD))
        st.latex(f"\\text{{Number of Anodes}} = {float(number_maxdis)}")

        left, right = st.columns([1,2])
        with right:
            st.text("\n*value taken from manufacturer data")

#=====================
#EQUATION 3
#=====================
st.header(" ")
st.header("Cable Resistance")
left, right = st.columns ([2,2])
#INPUT PARAMATERS
with left:
    with st.container(border=True):
        st.subheader("Input Parameters")

        Rcable = st.number_input("Resistance per km of cable (Ω/km) ", value=3, key="cable resistance")

        Lcable = st.number_input("Length in meters (sum of positive ad negative cables)", value=0.6, key="Lcable")
with right:
    with st.container(border=True):
        st.latex(
                 r"\text{Number} = "
                 r"\frac{\text{Cable Resistance per km x Cable Length}}{\text{1000}}")
        cres = (Rcable * Lcable)/1000
        st.latex(f"\\text{{Cable Resistance}} = {float(cres):.5f} Ω")

        


