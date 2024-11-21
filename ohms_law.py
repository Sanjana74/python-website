import streamlit as st

def compute_ohms():
    r = v / (i)
    return r


st.title("ohms law")

tab1, tab2 = st.tabs(["Compute", "Explain"])

with tab1:
    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            v = st.number_input("Enter Voltage value (V)", value=10.0)
            i = st.number_input("Enter Current value (i)", value=5.0)
            

    with col2:
        with st.container(border=True):
            r = compute_ohms()
            st.write("ohms law Results:")
            st.write(f"Resistance value={r} ohms") 
            

with tab2:
    st.write("Ohm’s law states that the voltage or potential difference between two points is directly proportional to the current or electricity passing through the resistance, and directly proportional to the resistance of the circuit.")