import streamlit as st
import pandas as pd
import yaml

option = st.selectbox(
    'Select Market or Country you want to config for output rules: ',
    ('UK', 'JE', "SG", 'HK hbap', "HK Hase")
)

with open("gb_config.yaml", 'r') as uploaded_config:
    loaded_config = yaml.safe_load(uploaded_config)

tab1, tab2, tab3 = st.tabs(["WPB", "CMB", "GBM"])

with tab1:
    st.header("WPB configuration")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.subheader("Threshold")
        aml_static_threshold = st.number_input('AML Static Threshold:', value=985)
        scc_hrtc_hram_threshold_factor = st.number_input('SCC/HTRC/HRAM factor:', value=0.95)
        ciiom_static_threshold = st.number_input('CIIOM threshold:', value=965)
        score_scale_factor = st.number_input('Score Scale factor: ', value=0.5)
    with col2:
        st.subheader("TBL")
        btl_wot_decile_num = st.number_input('BTL Decile Num:', value=16)
        ciiom_btl_sample_pool_size = st.number_input('CIIOM BTL Pool: ', value=4000)
        ciiom_btl_sample_size = st.number_input('CIIOM BTL Pool: ', value=7)
    with col3:
        st.subheader("Just BTL")
        jbtl_lower_bnd = st.number_input('JBTL Lower bound: ', value=946.07)
        jbtl_higher_bnd = st.number_input('JBTL Higher bound: ', value=985)
        jbtl_size = st.number_input('JBTL Size: ', value=120)
    with col4:
        st.subheader("Others")
        nta_cutoff = st.number_input('New Top activity cutoff: ', value=1)
        max_lookback_month = st.number_input('Lookback Month: ', value=6)
        go_live_month = st.text_input('Go-Live Month: ', '2021-10')
        first_batch_target_month = st.text_input('first batch target_month: ', '2021-10')
    st.subheader("Output Rules Settings:")
    wpb_includes_rules = st.multiselect(
        'Please select includes rules (wpb): ',
        ['gt_aml_threshold',
         'scc_customers',
         'gt_scc_threshold',
         'hrtc_customers',
         'gt_hrtc_customers',
         'hram_customers',
         'gt_hram_customers'
         ],
        ['gt_aml_threshold',
         'scc_customers',
         'gt_scc_threshold',
         'hrtc_customers',
         'gt_hrtc_customers',
         'hram_customers',
         'gt_hram_customers'])

    wpb_in_scope_rules = st.multiselect(
        'Please select in Scope rules (wpb): ',
        ['not_investigated',
         'score_gt_previous_case',
         'new_activity_since_previous_case',
         'BTL_WOT_Bin'
         ],
        ['not_investigated',
         'score_gt_previous_case',
         'new_activity_since_previous_case',
         'BTL_WOT_Bin']
    )

    wpb_btl_rules = st.multiselect(
        'Please select BTL rules (wpb): ',
        ['all_range_btl',
         'just_btl',
         'gb_ciiom_btl'
         ],
        ['all_range_btl',
         'just_btl',
         'gb_ciiom_btl']
    )

with tab2:
    st.header("CMB configuration")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.subheader("Threshold")
        cmb_aml_static_threshold = st.number_input('AML Static Threshold (cmb):', value=940)
        cmb_scc_hrtc_hram_threshold_factor = st.number_input('SCC/HTRC/HRAM factor (cmb):', value=0.95)
        cmb_ciiom_static_threshold = st.number_input('CIIOM threshold (cmb):', value=836)
        cmb_score_scale_factor = st.number_input('Score Scale factor (cmb): ', value=0.5)
        aar_static_threshold = st.number_input('AAR Static Threshold:', value=876)
        aar_ciiom_threshold = st.number_input('AAR CIIOM threshold:', value=775)
        aar_nrfb_threshold = st.number_input('AAR nRFB Threshold: ', value=823)
    with col2:
        st.subheader("TBL")
        cmb_btl_wot_decile_num = st.number_input('BTL Decile Num (cmb):', value=16)
        cmb_ciiom_btl_sample_pool_size = st.number_input('CIIOM BTL Pool (cmb): ', value=4000)
        cmb_ciiom_btl_sample_size = st.number_input('CIIOM BTL Pool (cmb): ', value=7)
    with col3:
        st.subheader("Just BTL")
        cmb_jbtl_lower_bnd = st.number_input('JBTL Lower bound (cmb): ', value=946.07)
        cmb_jbtl_higher_bnd = st.number_input('JBTL Higher bound (cmb): ', value=985)
        cmb_jbtl_size = st.number_input('JBTL Size (cmb): ', value=120)
    with col4:
        st.subheader("Others")
        cmb_nta_cutoff = st.number_input('New Top activity cutoff: ', value=1)
        cmb_max_lookback_month = st.number_input('Lookback Month: ', value=6)
        cmb_go_live_month = st.text_input('Go-Live Month: ', '2021-10')
        cmb_first_batch_target_month = st.text_input('first batch target_month: ', '2021-10')
    st.subheader("Output Rules Settings:")
    cmb_includes_rules = st.multiselect(
        'Please select includes rules (wpb): ',
        ['gt_aml_threshold',
         'scc_customers',
         'gt_scc_threshold',
         'hrtc_customers',
         'gt_hrtc_customers',
         'hram_customers',
         'gt_hram_customers'
         ],
        ['gt_aml_threshold',
         'scc_customers',
         'gt_scc_threshold',
         'hrtc_customers',
         'gt_hrtc_customers',
         'hram_customers',
         'gt_hram_customers'])

    cmb_in_scope_rules = st.multiselect(
        'Please select in Scope rules (wpb): ',
        ['not_investigated',
         'score_gt_previous_case',
         'new_activity_since_previous_case',
         'BTL_WOT_Bin'
         ],
        ['not_investigated',
         'score_gt_previous_case',
         'new_activity_since_previous_case',
         'BTL_WOT_Bin']
    )

    cmb_btl_rules = st.multiselect(
        'Please select BTL rules (wpb): ',
        ['all_range_btl',
         'just_btl',
         'gb_ciiom_btl'
         ],
        ['all_range_btl',
         'just_btl',
         'gb_ciiom_btl']
    )

    aar_includes_rules = st.multiselect(
        'Please select AAR includes rules: ',
        ['gt_aar_bl_aml_threshold',
         'aar_aml_investigation_in_last_12_months',
         'new_aar_activity_since_previous_case',
         'gt_aar_ciiom_threshold',
         'gt_aar_nrfb_threshold'
         ],
        ['gt_aar_bl_aml_threshold',
         'aar_aml_investigation_in_last_12_months',
         'new_aar_activity_since_previous_case',
         'gt_aar_ciiom_threshold',
         'gt_aar_nrfb_threshold'])

    aar_in_scope_rules = st.multiselect(
        'Please select AAR in_Scope rules: ',
        ['not_aar_aml_investigated_in_last_12_months',
         'new_activity_since_previous_case'
         ],
        ['not_aar_aml_investigated_in_last_12_months',
         'new_activity_since_previous_case'
         ]
    )

with tab3:
    st.header("GBM configuration")
    st.subheader("Output Rules Settings:")
    gbm_includes_rules = st.multiselect(
        'Please select includes rules (gbm): ',
        ['gt_aml_threshold',
         'scc_customers',
         'gt_scc_threshold',
         'hrtc_customers',
         'gt_hrtc_customers',
         'hram_customers',
         'gt_hram_customers'
         ],
        ['gt_aml_threshold',
         'scc_customers',
         'gt_scc_threshold',
         'hrtc_customers',
         'gt_hrtc_customers',
         'hram_customers',
         'gt_hram_customers'])

    gbm_in_scope_rules = st.multiselect(
        'Please select in Scope rules (gbm): ',
        ['not_investigated',
         'score_gt_previous_case',
         'new_activity_since_previous_case',
         'BTL_WOT_Bin'
         ],
        ['not_investigated',
         'score_gt_previous_case',
         'new_activity_since_previous_case',
         'BTL_WOT_Bin']
    )


txt = st.text_area("Please review configuration file:", value="output_rules:"
                                                              "wpb:"
                                                              "aml:"
                                                              "")
st.button("export conifg", type="primary")
st.download_button("Export configuration:", loaded_config,"gb_exported_config.yaml")