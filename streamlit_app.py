import streamlit as st
from Pages.Operator import operator_screen
from Pages.Technisian import technisian_screen

# Define the pages
def admin_page():
    st.title('Admin Page')
    st.write('This is the admin page.')
    if st.button('Logout',key='logout_btn_admin'):
        st.session_state.role = None
        st.rerun()

def operator_page():
    st.title('Operator Page')
    operator_screen()
    if st.button('Logout',key='logout_btn_operator'):
        st.session_state.role = None
        st.rerun()

def technician_page():
    st.title('Technician Page')
    technisian_screen()
    if st.button('Logout',key='logout_btn_technician'):
        st.session_state.role = None
        st.rerun()


# Initialize session state
if 'role' not in st.session_state:
    st.session_state.role = None

# Streamlit app
if st.session_state.role is None:

    st.title('Login Page')
    # Login form
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    login_button = st.button('Login',key='login_btn')

    if login_button:
        role = authenticate(username, password)
        if role:
            st.success(f'Welcome {username}!')
            st.session_state.role = role
            st.rerun()
        else:
            st.error('Invalid username or password')
else:
    if st.session_state.role == 'admin':
        admin_page()
    elif st.session_state.role == 'operator':
        operator_page()
    elif st.session_state.role == 'technician':
        technician_page()
