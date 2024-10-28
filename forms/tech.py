import streamlit as st


def tech_form():
    with st.form('aghlam_form'):
        col1,col2 = st.columns(2)
        with col1:
            technisian_numb1 = st.text_input('تکنیسین 1')
            technisian_numb2 = st.text_input('تکنیسین 2')
            technisian_numb3 = st.text_input('تکنیسین 3')
            technisian_numb4 = st.text_input('تکنیسین 4')
        with col2:
            technisian_numb5 = st.text_input('تکنیسین 5')
            technisian_numb6 = st.text_input('تکنیسین 6')
            technisian_numb7 = st.text_input('تکنیسین 7')
            technisian_numb8 = st.text_input('تکنیسین 8')                
            submit_button = st.form_submit_button('ثبت تکنیسین')
        
        
        if submit_button:
            st.success('Congratulations')