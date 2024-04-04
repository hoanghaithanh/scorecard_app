import streamlit as st

st.title('Credit Scoring Application')

st.markdown("""
    The application let you know your credit score based on the values filled in an Application Form, 
    which contains the following information group:
    * Demographic
    * Credit history
    * Financial Capability
    
    The Application Form requires you to answer 21 questions spread across 4 pages, from Page 1 to Page 4.
    In case you can not declare/find an appropriate answer, you can leave the field blank.
""")

st.sidebar.markdown("")
print("---------------APPLICATION INFORMATION---------------")

