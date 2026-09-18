import streamlit as st
import sympy as sp
from sympy import symbols, Function
import math
import pandas as pd

st.title("Galvanic Anode Life")

#====================
#EQUATION 1
#====================
st.header("Magnesium Galvanic Anode Life")
left, right = st.columns ([2,2])
#INPUT PARAMATERS
with left:
    with st.container(border=True):
        st.subheader("Input Parameters")

        Weight = st.number_input("Weight (Kg)", value=4, key="magweight")
        efficiency = st.number_input("Efficiency", value=0.8, key="effmaganode")
        UF = st.number_input("Utilisation Factor", value=0.85, key = "ufmaganode")
        current = st.number_input("Current (Amps)", value = 2, key = "currentmadanode")

with right:
    with st.container(border=True):
        st.latex(r"\text{Magnesium Years Life} = "r"\frac{\text{0.256 x Anode Wt. x Efficiency x Utilisation Factor}}{\text{Current}}")
        Mag_life = (0.256 * efficiency * Weight * UF)/(current)
        st.latex(f"\\text{{Magnesium Anode Life}} = {float(Mag_life):.2f} years")
       
#======================
# EQUATION 2
#======================
st.header("")
st.header("Zinc Galvanic Anode Life")
left, right = st.columns ([2,2])
#INPUT PARAMATERS
with left:
    with st.container(border=True):
        st.subheader("Input Parameters")

        Weightz = st.number_input("Weight (Kg)", value=25, key="zincweight")
        efficiencyz = st.number_input("Efficiency", value=0.8, key="effzincanode")
        UFz = st.number_input("Utilisation Factor", value=0.85, key = "ufzincanode")
        currentz = st.number_input("Current (Amps)", value = 10, key = "currentzincanode")

with right:
    with st.container(border=True):
        st.latex(r"\text{Zinc Years Life} = "r"\frac{\text{0.0935 x Anode Wt. x Efficiency x Utilisation Factor}}{\text{Current}}")
        Zinc_life = (0.0935 * efficiencyz * Weightz * UFz)/(currentz)
        st.latex(f"\\text{{Zinc Anode Life}} = {float(Zinc_life):.2f} years")


#====================
#DATA
#====================
Anodedata = pd.DataFrame({
    "Anode¹": [
        "Zinc",
        "Std. Mg",
        "Hi-Pot Mg"
    ],

    "Output² (Ahr/kg)": [
        815,
        1100,
        1100
    ],

    "Consumption Rate² (kg/Ahr)": [
        10.8,
        7.9,
        7.9
    ],

    "Efficiency²": [
        "90%",
        "50%",
        "50%"
    ],
    "Solution Potential³ (Cu-CuSO_4)": [
        "-1.1V",
        "-1.4 to -1.6V",
        "-1.7 to -1.8V"
    ]
})

st.header("")
st.header("Data")
st.dataframe(Anodedata, hide_index = True, use_container_width=True)

st.write("1. Anodes installed in suitable chemical backfill.")
st.write("2. Current efficiency with current density. The shown efficiency, and the resulting consumption rate, are at approximately 30 milliamps/ft² of anode surface.  Efficiencies are higher at higher current densities and lower at lower current densities.")
st.write("3. The potentials are solution potentials. When calculating driving potentials, the difference between the protected structure and the anode, allow for anode polarization. Anode polarization is also influenced by current density at the anode surface. For magnesium polarization allow for 0.1 V anodic polarization. Zinc in a proper backfill is not usually subject to significant anodic polarization and the solution potential may be used.")


     