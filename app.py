import streamlit as st
import pandas as pd

option = st.selectbox(
    'Select Market or Country you want to config for output rules: ',
    ('UK', 'JE', "SG", 'HK hbap', "HK Hase")
)

tab1, tab2, tab3 = st.tabs(["WPB", "CMB", "GBM"])

with tab1:
    st.header("WPB configuration")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.subheader("Threshold")
        aml_static_threshold = st.number_input('AML Static Threshold:', value=985)
    with col2:
        st.subheader("TBL")
        btl_wot_decile_num = st.number_input('BTL Decile Num:', value=16)
    with col3:
        st.subheader("Just BTL")
        jbtl_lower_bnd = st.number_input('Just BTL Lower bound: ', value=946.07)
    with col4:
        st.subheader("Others")
        nta_cutoff = st.number_input('New Top activity cutoff: ', value=1)
    st.subheader("Output Rules Settings:")
    wbp_includes_rules = st.multiselect(
        'Please select rules for wpb includes: ',
        ['scc_customers',
         'gt_scc_threshold'],
        ['scc_customers']
    )
with tab2:
    st.header("CMB configuration")
with tab3:
    st.header("GBM configuration")


st.button("export conifg", type="primary")
st.button("welcome!")