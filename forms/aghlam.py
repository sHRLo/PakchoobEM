import streamlit as st



def aghlam_form():
    with st.form('aghlam_form'):
        form_code = st.text_input('کد درخواست')
        form_date = st.date_input('تاریخ')
        form_discription = st.text_input('شرح قلم')
        form_numb = st.text_input('تعداد قلم')
        form_unit = st.selectbox('نوع قلم', options=['عدد','متر','سانتی متر','میلی متر','گرم','کیلوگرم','لیتر'])
        submit_button = st.form_submit_button('ثبت اقلام')
        
        if submit_button:
            st.success('Nice')
