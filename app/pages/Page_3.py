import streamlit as st
import pandas as pd
import numpy as np
from util import general as uf

st.title('Application Form')

print("---------------PAGE 3---------------")

input = uf.load_input()
default_placeholder = "Declare the value here"

# mths_since_last_delinq
desc11 = "The number of months since the borrower's last delinquency."
label11 = "Q11: "+desc11
ft11_value = st.text_input(label=label11, placeholder=default_placeholder,
                           value=input[desc11], label_visibility="visible")
print(label11, ft11_value)
input[desc11] = uf.convert_to_INT(ft11_value)

# mths_since_last_record
desc12 = "The number of months since the last public record."
label12 = "Q12: "+desc12
ft12_value = st.text_input(label=label12, placeholder=default_placeholder,
                           value=input[desc12], label_visibility="visible")
print(label12, ft12_value)
input[desc12] = uf.convert_to_INT(ft12_value)

# open_acc
desc13 = "The number of open credit lines in the borrower's credit file."
label13 = "Q13: "+desc13
ft13_value = st.text_input(label=label13, placeholder=default_placeholder,
                           value=input[desc13], label_visibility="visible")
print(label13, ft13_value)
input[desc13] = uf.convert_to_INT(ft13_value)

# revol_util
desc14 = "Revolving line utilization rate, or the amount of credit the borrower is using relative to all available revolving credit."
label14 = "Q14: "+desc14
ft14_value = st.text_input(label=label14, placeholder=default_placeholder,
                           value=input[desc14], label_visibility="visible")
print(label14, ft14_value)
input[desc14] = uf.convert_to_FLOAT(ft14_value)

# total_acc
desc15 = "The total number of credit lines currently in the borrower's credit file"
label15 = "Q15: "+desc15
ft15_value = st.text_input(label=label15, placeholder=default_placeholder,
                           value=input[desc15], label_visibility="visible")
print(label15, ft15_value)
input[desc15] = uf.convert_to_INT(ft15_value)

# save button
if st.button(label="Save", type="secondary"):
    uf.save_input(input)