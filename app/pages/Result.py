import streamlit as st
import pandas as pd
import numpy as np
from util import features_engineering as ufe
from util import general as uf
from util import visualization as uv

input = uf.load_input()

base_score = 452
min_score, max_score = uf.retrieve_min_max_credit_score(base_score)

# 1. term
desc1 = "The number of payments on the loan. Values are in months and can be either 36 or 60."
term = ufe.retrieve_TERM_score(input, desc1)

# 2. emp_length
desc2 = "Employment length in years. Possible values are between 0 and 10 where 0 means less than one year and 10 means ten or more years."
emp_length = ufe.retrieve_EMP_LENGTH_score(input, desc2)

# 3. home_ownership
desc3 = "The home ownership status provided by the borrower during registration or obtained from the credit report. Our values are: RENT, OWN, MORTGAGE, OTHER"
home_ownership = ufe.retrieve_HOME_OWNERSHIP_score(input, desc3)

# 4. purpose
desc4 = "A category provided by the borrower for the loan request."
purpose = ufe.retrieve_PURPOSE_score(input, desc4)

# 5. initial_list_status
desc5 = "The initial listing status of the loan. Possible values are – W, F"
initial_list_status = ufe.retrieve_INITIAL_LIST_STATUS_score(input, desc5)

# 6. loan_amnt
desc6 = "The listed amount of the loan applied for by the borrower. If at some point in time, the credit department reduces the loan amount, then it will be reflected in this value."
loan_amnt = ufe.retrieve_LOAN_AMNT_score(input, desc6)

# 7. int_rate
desc7 = "Interest Rate on the loan"
int_rate = ufe.retrieve_INT_RATE_score(input, desc7)

# 8. installment
desc8 = "The monthly payment owed by the borrower if the loan originates."
installment = ufe.retrieve_INSTALLMENT_score(input, desc8)

# 9. dti
desc9 = "A ratio calculated using the borrower's total monthly debt payments on the total debt obligations, excluding mortgage and the requested LC loan, divided by the borrower's self-reported monthly income."
dti = ufe.retrieve_DTI_score(input, desc9)

# 10. inq_last_6mths
desc10 = "The number of inquiries in past 6 months (excluding auto and mortgage inquiries)"
inq_last_6mths = ufe.retrieve_INQ_LAST_6MTHS_score(input, desc10)

# 11. mths_since_last_delinq
desc11 = "The number of months since the borrower's last delinquency."
mths_since_last_delinq = ufe.retrieve_MTHS_SINCE_LAST_DELINQ_score(input, desc11)

# 12. mths_since_last_record
desc12 = "The number of months since the last public record."
mths_since_last_record = ufe.retrieve_MTHS_SINCE_LAST_RECORD_score(input, desc12)

# 13. open_acc
desc13 = "The number of open credit lines in the borrower's credit file."
open_acc = ufe.retrieve_OPEN_ACC_score(input, desc13)

# 14. revol_util
desc14 = "Revolving line utilization rate, or the amount of credit the borrower is using relative to all available revolving credit."
revol_util = ufe.retrieve_REVOL_UTIL_score(input, desc14)

# 15. total_acc
desc15 = "The total number of credit lines currently in the borrower's credit file"
total_acc = ufe.retrieve_TOTAL_ACC_score(input, desc15)

# 16. total_rec_prncp
desc16 = "Principal received to date"
total_rec_prncp = ufe.retrieve_TOTAL_REC_PRNCP_score(input, desc16)

# 17. total_rec_int
desc17 = "Interest received to date"
total_rec_int = ufe.retrieve_TOTAL_REC_INT_score(input, desc17)

# 18. last_pymnt_amnt
desc18 = "Last total payment amount received"
last_pymnt_amnt = ufe.retrieve_LAST_PYMNT_AMNT_score(input, desc18)

# 19. mths_since_last_major_derog
desc19 = "Months since most recent 90-day or worse rating"
mths_since_last_major_derog = ufe.retrieve_MTHS_SINCE_LAST_MAJOR_DEROG_score(input, desc19)

# 20. tot_cur_bal
desc20 = "Total current balance of all accounts"
tot_cur_bal = ufe.retrieve_TOT_CUR_BAL_score(input, desc20)

# 21. total_rev_hi_lim
desc21 = "Total revolving high credit/credit limit"
total_rev_hi_lim = ufe.retrieve_TOTAL_REV_HI_LIM_score(input, desc21)

# adding up to generate final credit score
print(f"""
base_score: {str(base_score)}, 
term: {str(term)}, 
emp_length: {str(emp_length)}, 
home_ownership: {str(home_ownership)}, 
purpose: {str(purpose)}, 
initial_list_status: {str(initial_list_status)}, 
loan_amnt: {str(loan_amnt)}, 
int_rate: {str(int_rate)}, 
installment: {str(installment)}, 
dti: {str(dti)}, 
inq_last_6mths: {str(inq_last_6mths)}, 
mths_since_last_delinq: {str(mths_since_last_delinq)}, 
mths_since_last_record: {str(mths_since_last_record)}, 
open_acc: {str(open_acc)}, 
revol_util: {str(revol_util)}, 
total_acc: {str(total_acc)}, 
total_rec_prncp: {str(total_rec_prncp)}, 
total_rec_int: {str(total_rec_int)}, 
last_pymnt_amnt: {str(last_pymnt_amnt)}, 
mths_since_last_major_derog: {str(mths_since_last_major_derog)}, 
tot_cur_bal: {str(tot_cur_bal)}, 
total_rev_hi_lim: {str(total_rev_hi_lim)}, 
""")

credit_score = base_score + term + emp_length + home_ownership + purpose + \
               initial_list_status + loan_amnt + int_rate + installment + dti + \
               inq_last_6mths + mths_since_last_delinq + mths_since_last_record + \
               open_acc + revol_util + total_acc + total_rec_prncp + total_rec_int + \
               last_pymnt_amnt + mths_since_last_major_derog + tot_cur_bal + total_rev_hi_lim

print(min_score, max_score, credit_score)

gauge_fig = uv.create_gauge_chart(credit_score, min_score, max_score)
st.plotly_chart(gauge_fig, use_container_width=True)

