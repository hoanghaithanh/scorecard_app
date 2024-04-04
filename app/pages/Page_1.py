import streamlit as st
import pandas as pd
import numpy as np
from util import general as uf

st.title('Application Form')

print("---------------PAGE 1---------------")

input = uf.load_input()
default_placeholder = "Declare the value here"

# term
desc1 = "The number of payments on the loan. Values are in months and can be either 36 or 60."
label1 = "Q1: "+desc1
options1 = ("36 months", "60 months")
ft1_value = st.selectbox(label=label1, placeholder=default_placeholder,
                         index=uf.find_index(input[desc1], options1),
                         label_visibility="visible", options=options1)
print(label1, ft1_value)
input[desc1] = ft1_value

# emp_length
desc2 = "Employment length in years. Possible values are between 0 and 10 where 0 means less than one year and 10 means ten or more years."
label2 = "Q2: "+desc2
options2 = ("< 1 year", "1 year", "2 years", "3 years", "4 years", "5 years", "6 years",
            "7 years", "8 years", "9 years", "10+ years")
ft2_value = st.selectbox(label=label2, placeholder=default_placeholder,
                         index=uf.find_index(input[desc2], options2),
                         label_visibility="visible", options=options2)
print(label2, ft2_value)
input[desc2] = ft2_value

# home_ownership
desc3 = "The home ownership status provided by the borrower during registration or obtained from the credit report. Our values are: RENT, OWN, MORTGAGE, OTHER"
label3 = "Q3: "+desc3
options3 = ("MORTGAGE", "OWN", "RENT")
ft3_value = st.selectbox(label=label3, placeholder=default_placeholder,
                         index=uf.find_index(input[desc3], options3),
                         label_visibility="visible", options=options3)
print(label3, ft3_value)
input[desc3] = ft3_value

# purpose
desc4 = "A category provided by the borrower for the loan request."
label4 = "Q4: "+desc4
options4 = ("house", "home_improvement", "car", "credit_card", "debt_consolidation",
            "vacation", "moving", "major_purchase", "medical", "small_business",
            "renewable_energy", "wedding", "other")
ft4_value = st.selectbox(label=label4, placeholder=default_placeholder,
                         index=uf.find_index(input[desc4], options4),
                         label_visibility="visible", options=options4)
print(label4, ft4_value)
input[desc4] = ft4_value

# initial_list_status
desc5 = "The initial listing status of the loan. Possible values are – W, F"
label5 = "Q5: "+desc5
options5 = ("W", "F")
ft5_value = st.selectbox(label=label5, placeholder=default_placeholder,
                         index=uf.find_index(input[desc5], options5),
                         label_visibility="visible", options=options5)
print(label5, ft5_value)
input[desc5] = ft5_value

# save button
if st.button(label="Save", type="secondary"):
    uf.save_input(input)