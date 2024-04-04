import streamlit as st
import pandas as pd
import numpy as np
from util import general as uf

st.title('Application Form')

print("---------------PAGE 2---------------")

input = uf.load_input()
default_placeholder = "Declare the value here"

# loan_amnt
desc6 = "The listed amount of the loan applied for by the borrower. If at some point in time, the credit department reduces the loan amount, then it will be reflected in this value."
label6 = "Q6: "+desc6
ft6_value = st.text_input(label=label6, placeholder=default_placeholder,
                          value=input[desc6], label_visibility="visible")
print(label6, ft6_value)
input[desc6] = uf.convert_to_FLOAT(ft6_value)

# int_rate
desc7 = "Interest Rate on the loan"
label7 = "Q7: "+desc7
ft7_value = st.text_input(label=label7, placeholder=default_placeholder,
                          value=input[desc7], label_visibility="visible")
print(label7, ft7_value)
input[desc7] = uf.convert_to_FLOAT(ft7_value)

# installment
desc8 = "The monthly payment owed by the borrower if the loan originates."
label8 = "Q8: "+desc8
ft8_value = st.text_input(label=label8, placeholder=default_placeholder,
                          value=input[desc8], label_visibility="visible")
print(label8, ft8_value)
input[desc8] = uf.convert_to_FLOAT(ft8_value)

# dti
desc9 = "A ratio calculated using the borrower's total monthly debt payments on the total debt obligations, excluding mortgage and the requested LC loan, divided by the borrower's self-reported monthly income."
label9 = "Q9: "+desc9
ft9_value = st.text_input(label=label9, placeholder=default_placeholder,
                          value=input[desc9], label_visibility="visible")
print(label9, ft9_value)
input[desc9] = uf.convert_to_FLOAT(ft9_value)

# inq_last_6mths
desc10 = "The number of inquiries in past 6 months (excluding auto and mortgage inquiries)"
label10 = "Q10: "+desc10
ft10_value = st.text_input(label=label10, placeholder=default_placeholder,
                           value=input[desc10], label_visibility="visible")
print(label10, ft10_value)
input[desc10] = uf.convert_to_INT(ft10_value)

# save button
if st.button(label="Save", type="secondary"):
    uf.save_input(input)