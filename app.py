import os

import streamlit as st
import pandas as pd
import yaml
import sys
market_option = st.selectbox(
    'Select Market or Country you want to config for output rules: ',
    ('GB', 'JE', "SG", 'HK_HSBC', "HK_HASE")
)

with open(os.path.join(os.path.dirname(sys.argv[0]), market_option.lower()+"_config.yaml"), 'r') as uploaded_config:
    loaded_config = yaml.load(uploaded_config, Loader=yaml.FullLoader)

tab1, tab2, tab3 = st.tabs(["WPB", "CMB", "GBM"])


with tab1:
    st.header("WPB configuration")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.subheader("Threshold")
        aml_static_threshold = st.number_input('AML Static Threshold: ', value=loaded_config['output_rules']['wpb']['aml']['static_threshold'])
        scc_hrtc_hram_threshold_factor = st.number_input('SCC/HTRC/HRAM factor: ', value=loaded_config['output_rules']['wpb']['aml']['scc_hrtc_hram_threshold_factor'])
        ciiom_static_threshold = st.number_input('CIIOM threshold: ', value=loaded_config['output_rules']['wpb']['aml']['ciiom_static_threshold'])
        score_scale_factor = st.number_input('Score Scale factor: ', value=loaded_config['output_rules']['wpb']['aml']['score_scale_factor'])

    with col2:
        st.subheader("BTL")
        btl_wot_decile_num = st.number_input('BTL Decile Num:', value=loaded_config['output_rules']['wpb']['aml']['btl_wot_decile_num'])
        ciiom_btl_sample_pool_size = st.number_input('CIIOM BTL Pool: ', value=loaded_config['output_rules']['wpb']['aml']['ciiom_btl_sample_pool_size'])
        ciiom_btl_sample_size = st.number_input('CIIOM BTL Pool: ', value=loaded_config['output_rules']['wpb']['aml']['ciiom_btl_sample_size'])

    with col3:
        st.subheader("Just BTL")
        jbtl_lower_bnd = st.number_input('JBTL Lower bound: ', value=loaded_config['output_rules']['wpb']['aml']['jbtl_lower_bnd'])
        jbtl_higher_bnd = st.number_input('JBTL Higher bound: ', value=loaded_config['output_rules']['wpb']['aml']['jbtl_higher_bnd'])
        jbtl_size = st.number_input('JBTL Size: ', value=loaded_config['output_rules']['wpb']['aml']['jbtl_size'])

    with col4:
        st.subheader("Others")
        nta_cutoff = st.number_input('New Top activity cutoff: ', value=loaded_config['output_rules']['wpb']['aml']['nta_cutoff'])
        max_lookback_month = st.number_input('Lookback Month: ', value=loaded_config['output_rules']['wpb']['aml']['max_lookback_month'])
        go_live_month = st.text_input('Go-Live Month: ', loaded_config['output_rules']['wpb']['aml']['go_live_month'])
        first_batch_target_month = st.text_input('first batch target_month: ', loaded_config['output_rules']['wpb']['aml']['first_batch_target_month'])

    st.subheader("Output Rules Settings:")
    wpb_includes_rules = st.multiselect(
        'Please select includes rules (wpb): ',
        [loaded_config['output_rules']['wpb']['aml']['go_live_month_rules']],
        [loaded_config['output_rules']['wpb']['aml']['go_live_month_rules']]
    )

    wpb_in_scope_rules = st.multiselect(
        'Please select in Scope rules (wpb): ',
        [loaded_config['output_rules']['wpb']['aml']['post_go_live_month_rules']],
        [loaded_config['output_rules']['wpb']['aml']['post_go_live_month_rules']]
    )

    wpb_btl_rules = st.multiselect(
        'Please select BTL rules (wpb): ',
        loaded_config['output_rules']['wpb']['aml']['btl_rules'],
        loaded_config['output_rules']['wpb']['aml']['btl_rules']
    )

with tab2:
    st.header("CMB configuration")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.subheader("Threshold")
        cmb_aml_static_threshold = st.number_input('AML Static Threshold (cmb):', value=loaded_config['output_rules']['cmb']['aml']['static_threshold'])
        cmb_scc_hrtc_hram_threshold_factor = st.number_input('SCC/HTRC/HRAM factor (cmb):', value=loaded_config['output_rules']['cmb']['aml'][
                                                             'scc_hrtc_hram_threshold_factor'])
        cmb_ciiom_static_threshold = st.number_input('CIIOM threshold (cmb):', value=loaded_config['output_rules']['cmb']['aml'][
            'ciiom_static_threshold'])
        cmb_score_scale_factor = st.number_input('Score Scale factor (cmb): ', value=loaded_config['output_rules']['cmb']['aml']['score_scale_factor'])
        aar_static_threshold = st.number_input('AAR Static Threshold:', value=loaded_config['output_rules']['cmb']['aar']['aar_static_threshold'])
        aar_ciiom_threshold = st.number_input('AAR CIIOM threshold:', value=loaded_config['output_rules']['cmb']['aar']['aar_ciiom_threshold'])
        aar_nrfb_threshold = st.number_input('AAR nRFB Threshold: ', value=loaded_config['output_rules']['cmb']['aar']['aar_nrfb_threshold'])
    with col2:
        st.subheader("BTL")
        cmb_btl_wot_decile_num = st.number_input('BTL Decile Num (cmb):', value=loaded_config['output_rules']['cmb']['aml']['btl_wot_decile_num'])
        cmb_ciiom_btl_sample_pool_size = st.number_input('CIIOM BTL Pool (cmb): ', value=loaded_config['output_rules']['cmb']['aml']['ciiom_btl_sample_pool_size'])
        cmb_ciiom_btl_sample_size = st.number_input('CIIOM BTL Pool (cmb): ', value=loaded_config['output_rules']['cmb']['aml']['ciiom_btl_sample_size'])
    with col3:
        st.subheader("Just BTL")
        cmb_jbtl_lower_bnd = st.number_input('JBTL Lower bound (cmb): ', value=loaded_config['output_rules']['cmb']['aml']['jbtl_lower_bnd'])
        cmb_jbtl_higher_bnd = st.number_input('JBTL Higher bound (cmb): ', value=loaded_config['output_rules']['cmb']['aml']['jbtl_higher_bnd'])
        cmb_jbtl_size = st.number_input('JBTL Size (cmb): ', value=loaded_config['output_rules']['cmb']['aml']['jbtl_size'])
    with col4:
        st.subheader("Others")
        cmb_nta_cutoff = st.number_input('New Top activity cutoff (cmb): ', value=loaded_config['output_rules']['cmb']['aml']['nta_cutoff'])
        cmb_max_lookback_month = st.number_input('Lookback Month (cmb): ', value=loaded_config['output_rules']['cmb']['aml']['max_lookback_month'])
        cmb_go_live_month = st.text_input('Go-Live Month (cmb): ', loaded_config['output_rules']['cmb']['aml']['go_live_month'])
        cmb_first_batch_target_month = st.text_input('first batch target_month (cmb): ', loaded_config['output_rules']['cmb']['aml']['first_batch_target_month'])
    st.subheader("Output Rules Settings:")
    cmb_includes_rules = st.multiselect(
        'Please select includes rules (cmb): ',
        [loaded_config['output_rules']['cmb']['aml']['go_live_month_rules']],
        [loaded_config['output_rules']['cmb']['aml']['go_live_month_rules']])

    cmb_in_scope_rules = st.multiselect(
        'Please select in Scope rules (cmb): ',
        [loaded_config['output_rules']['cmb']['aml']['post_go_live_month_rules']],
        [loaded_config['output_rules']['cmb']['aml']['post_go_live_month_rules']]
    )

    cmb_btl_rules = st.multiselect(
        'Please select BTL rules (cmb): ',
        loaded_config['output_rules']['cmb']['aml']['btl_rules'],
        loaded_config['output_rules']['cmb']['aml']['btl_rules']
    )

    aar_includes_rules = st.multiselect(
        'Please select AAR includes rules: ',
        loaded_config['output_rules']['cmb']['aar']['aar_include_rules'],
        loaded_config['output_rules']['cmb']['aar']['aar_include_rules'])

    aar_in_scope_rules = st.multiselect(
        'Please select AAR in_Scope rules: ',
        loaded_config['output_rules']['cmb']['aar']['aar_in_scope_rules'],
        loaded_config['output_rules']['cmb']['aar']['aar_in_scope_rules']
    )

with tab3:
    st.header("GBM configuration")
    st.subheader("Output Rules Settings:")

    gbm_includes_rules = st.multiselect(
        'Please select includes rules (gbm): ',
        [loaded_config['output_rules']['gbm']['aml']['go_live_month_rules']],
        [loaded_config['output_rules']['gbm']['aml']['go_live_month_rules']])

    gbm_in_scope_rules = st.multiselect(
        'Please select in Scope rules (gbm): ',
        [loaded_config['output_rules']['gbm']['aml']['post_go_live_month_rules']],
        [loaded_config['output_rules']['gbm']['aml']['post_go_live_month_rules']]
    )



# update the settings:
# wpb
loaded_config['output_rules']['wpb']['aml']['static_threshold'] = aml_static_threshold
loaded_config['output_rules']['wpb']['aml']['scc_hrtc_hram_threshold_factor'] = scc_hrtc_hram_threshold_factor
loaded_config['output_rules']['wpb']['aml']['ciiom_static_threshold'] = ciiom_static_threshold
loaded_config['output_rules']['wpb']['aml']['score_scale_factor'] = score_scale_factor
loaded_config['output_rules']['wpb']['aml']['btl_wot_decile_num'] = btl_wot_decile_num
loaded_config['output_rules']['wpb']['aml']['ciiom_btl_sample_pool_size'] = ciiom_btl_sample_pool_size
loaded_config['output_rules']['wpb']['aml']['ciiom_btl_sample_size'] = ciiom_btl_sample_size
loaded_config['output_rules']['wpb']['aml']['jbtl_lower_bnd'] = jbtl_lower_bnd
loaded_config['output_rules']['wpb']['aml']['jbtl_higher_bnd'] = jbtl_higher_bnd
loaded_config['output_rules']['wpb']['aml']['jbtl_size'] = jbtl_size
loaded_config['output_rules']['wpb']['aml']['nta_cutoff'] = nta_cutoff
loaded_config['output_rules']['wpb']['aml']['max_lookback_month'] = max_lookback_month
loaded_config['output_rules']['wpb']['aml']['go_live_month'] = go_live_month
loaded_config['output_rules']['wpb']['aml']['first_batch_target_month'] = first_batch_target_month
loaded_config['output_rules']['wpb']['aml']['go_live_month_rules'] = wpb_includes_rules
loaded_config['output_rules']['wpb']['aml']['post_go_live_month_rules'] = wpb_in_scope_rules
loaded_config['output_rules']['wpb']['aml']['btl_rules'] = wpb_btl_rules

# cmb
loaded_config['output_rules']['cmb']['aml']['static_threshold'] = cmb_aml_static_threshold
loaded_config['output_rules']['cmb']['aml']['scc_hrtc_hram_threshold_factor'] = cmb_scc_hrtc_hram_threshold_factor
loaded_config['output_rules']['cmb']['aml']['ciiom_static_threshold'] = cmb_ciiom_static_threshold
loaded_config['output_rules']['cmb']['aml']['score_scale_factor'] = cmb_score_scale_factor
loaded_config['output_rules']['cmb']['aar']['aar_static_threshold'] = aar_static_threshold
loaded_config['output_rules']['cmb']['aar']['aar_ciiom_threshold'] = aar_ciiom_threshold
loaded_config['output_rules']['cmb']['aar']['aar_nrfb_threshold'] = aar_nrfb_threshold
loaded_config['output_rules']['cmb']['aml']['btl_wot_decile_num'] = cmb_btl_wot_decile_num
loaded_config['output_rules']['cmb']['aml']['ciiom_btl_sample_pool_size'] = cmb_ciiom_btl_sample_pool_size
loaded_config['output_rules']['cmb']['aml']['ciiom_btl_sample_size'] = cmb_ciiom_btl_sample_size
loaded_config['output_rules']['cmb']['aml']['jbtl_lower_bnd'] = cmb_jbtl_lower_bnd
loaded_config['output_rules']['cmb']['aml']['jbtl_higher_bnd'] = cmb_jbtl_higher_bnd
loaded_config['output_rules']['cmb']['aml']['jbtl_size'] = cmb_jbtl_size
loaded_config['output_rules']['cmb']['aml']['nta_cutoff'] = cmb_nta_cutoff
loaded_config['output_rules']['cmb']['aml']['max_lookback_month'] = cmb_max_lookback_month
loaded_config['output_rules']['cmb']['aml']['go_live_month'] = cmb_go_live_month
loaded_config['output_rules']['cmb']['aml']['first_batch_target_month'] = cmb_first_batch_target_month
loaded_config['output_rules']['cmb']['aml']['go_live_month_rules'] = cmb_includes_rules
loaded_config['output_rules']['cmb']['aml']['post_go_live_month_rules'] = cmb_in_scope_rules
loaded_config['output_rules']['cmb']['aml']['btl_rules'] = cmb_btl_rules
loaded_config['output_rules']['cmb']['aar']['aar_include_rules'] = aar_includes_rules
loaded_config['output_rules']['cmb']['aar']['aar_in_scope_rules'] = aar_in_scope_rules

# gbm
loaded_config['output_rules']['gbm']['aml']['go_live_month_rules'] = gbm_includes_rules
loaded_config['output_rules']['gbm']['aml']['post_go_live_month_rules'] = gbm_in_scope_rules

# show the yaml txt:
css = '''
<style>
    .element-container:has(>.stTextArea), .stTextArea {
        width: 800px !important;
    }
    .stTextArea textarea {
        height: 400px;
    }
</style>
'''
st.text_area("Please review configuration file:", value=loaded_config)
st.write(css, unsafe_allow_html=True)



st.download_button("Export configuration:", yaml.dump(loaded_config,allow_unicode=True), market_option.lower()+"_config.yaml")