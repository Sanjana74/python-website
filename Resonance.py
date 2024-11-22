import streamlit as st
import numpy as np

st.title('Series RLC Circuit Calculator')

st.write('This app calculates the resonance frequency, bandwidth, quality factor, upper cutoff frequency, and lower cutoff frequency for a series RLC circuit.')

R = st.number_input('Enter the resistance (R) in ohms:', min_value=0.0, format="%.2f")
L = st.number_input('Enter the inductance (L) in henrys:', min_value=0.0, format="%.2f")
C = st.number_input('Enter the capacitance (C) in farads:', min_value=0.0, format="%.2f")

if st.button('Calculate'):
    if R > 0 and L > 0 and C > 0:
        f0 = 1 / (2 * np.pi * np.sqrt(L * C))
        Q = (1 / R) * np.sqrt(L / C)
        bandwidth = f0 / Q
        fcu = f0 + (bandwidth / 2)
        fcl = f0 - (bandwidth / 2)

        st.write(f'Resonance frequency: {f0:.2f} Hz')
        st.write(f'Quality factor: {Q:.2f}')
        st.write(f'Bandwidth: {bandwidth:.2f} Hz')
        st.write(f'Upper cutoff frequency: {fcu:.2f} Hz')
        st.write(f'Lower cutoff frequency: {fcl:.2f} Hz')
    else:
        st.write('Please enter positive values for R, L, and C.')

