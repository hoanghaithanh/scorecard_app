import streamlit as st
import pandas as pd
import numpy as np
from util import general as uf

st.title('Application Form')

print("---------------PAGE 4---------------")

input = uf.load_input()
default_placeholder = "Declare the value here"

# total_rec_prncp
desc16 = "Principal received to date"
label16 = "Q16: "+desc16
ft16_value = st.text_input(label=label16, placeholder=default_placeholder,
                           value=input[desc16], label_visibility="visible")
print(label16, ft16_value)
input[desc16] = uf.convert_to_FLOAT(ft16_value)

# total_rec_int
desc17 = "Interest received to date"
label17 = "Q17: "+desc17
ft17_value = st.text_input(label=label17, placeholder=default_placeholder,
                           value=input[desc17], label_visibility="visible")
print(label17, ft17_value)
input[desc17] = uf.convert_to_FLOAT(ft17_value)

# last_pymnt_amnt
desc18 = "Last total payment amount received"
label18 = "Q18: "+desc18
ft18_value = st.text_input(label=label18, placeholder=default_placeholder,
                           value=input[desc18], label_visibility="visible")
print(label18, ft18_value)
input[desc18] = uf.convert_to_FLOAT(ft18_value)

# mths_since_last_major_derog
desc19 = "Months since most recent 90-day or worse rating"
label19 = "Q19: "+desc19
ft19_value = st.text_input(label=label19, placeholder=default_placeholder,
                           value=input[desc19], label_visibility="visible")
print(label19, ft19_value)
input[desc19] = uf.convert_to_INT(ft19_value)

# tot_cur_bal
desc20 = "Total current balance of all accounts"
label20 = "Q20: "+desc20
ft20_value = st.text_input(label=label20, placeholder=default_placeholder,
                           value=input[desc20], label_visibility="visible")
print(label20, ft20_value)
input[desc20] = uf.convert_to_FLOAT(ft20_value)

# total_rev_hi_lim
desc21 = "Total revolving high credit/credit limit"
label21 = "Q21: "+desc21
ft21_value = st.text_input(label=label21, placeholder=default_placeholder,
                           value=input[desc21], label_visibility="visible")
print(label21, ft21_value)
input[desc21] = uf.convert_to_FLOAT(ft21_value)

# save button
if st.button(label="Save", type="secondary"):
    uf.save_input(input)