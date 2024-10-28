import streamlit as st

def operator_screen():
    container_operator = st.container(height=None,border=True,key=None)

    container_operator.subheader('این قسمت توسط اپراتور انجام می شود')
    container_operator.text_input('شماره درخواست',key='form_code')
    container_operator.selectbox('نام واحد',options=['Chipper',
                                                    'Conveyor Line',
                                                    'Energy Plant',
                                                    'Dryer & Air Grader',
                                                    'Refiner',
                                                    'Before Press',
                                                    'Press',
                                                    'After Press',
                                                    'Sanding & RBS',
                                                    'Cooling System'
                                                    'Steam Boiler',
                                                    'General'
                                                    ],key='section_name')
    container_operator.text_input('مشخصات دستگاه',key='machine_name')
    container_operator.selectbox('شیفت',options=[
                                                'A',
                                                'B',
                                                'C'
                                                ],key='shift')
    container_operator.text_input('نام درخواست کننده',key='operator')
    container_operator.selectbox('نوع عیب',options=[
                                                    'مکانیکی',
                                                    'برقی',
                                                    'تولید',
                                                    'تاسیسات',
                                                    'فلزکاری'
                                                    ])
    container_operator.subheader('تعیین زمان بروز اشکال')
    container_operator.selectbox('وضعیت توقف',options=['ندارد','دارد'])
    container_operator.date_input('زمان شروع توقف',key='stop',format="YYYY/MM/DD")
    container_operator.date_input('زمان پایان توقف',key='start')

    if container_operator.button('ثبت',key='operator_section'):
        st.success('Everything Works Fine')

operator_screen()

