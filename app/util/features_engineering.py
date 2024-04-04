import pandas as pd
import numpy as np

# 1. TERM
def retrieve_TERM_score(input, desc):
    value = input[desc]
    score = 0
    if (value != "") and (value != None):
        if value == "36 months":
            score = -39
        elif value == "36 months":
            score = 73
    return score

# 2. EMP_LENGTH
def retrieve_EMP_LENGTH_score(input, desc):
    value = input[desc]
    score = 0
    if (value == "") or (value == None):
        score = -16
    elif value == "10+ years":
        score = 8
    elif value in ("8 years", "9 years"):
        score = 4
    elif value in ("6 years", "3 years", "2 years", "7 years"):
        score = -1
    elif value in ("4 years", "5 years", "< 1 year", "1 year"):
        score = -6
    return score

# 3. HOME_OWNERSHIP
def retrieve_HOME_OWNERSHIP_score(input, desc):
    value = input[desc]
    score = 0
    if (value != "") and (value != None):
        if value == "MORTGAGE":
            score = 4
        elif value == "OWN":
            score = 1
        elif value == "RENT":
            score = -5
    return score

# 4. PURPOSE
def retrieve_PURPOSE_score(input, desc):
    value = input[desc]
    score = 0
    if (value != "") and (value != None):
        if value in ("house", "home_improvement", "car"):
            score = -4
        elif value == "credit_card":
            score = -2
        elif value in ("other", "debt_consolidation", "vacation"):
            score = 0
        elif value in ("moving", "major_purchase", "medical", "small_business",
                       "renewable_energy", "wedding"):
            score = 4
    return score

# 5. INITIAL_LIST_STATUS
def retrieve_INITIAL_LIST_STATUS_score(input, desc):
    value = input[desc]
    score = 0
    if (value != "") and (value != None):
        if value == "W":
            score = 5
        elif value == "F":
            score = -5
    return score

# 6. LOAN_AMNT
def retrieve_LOAN_AMNT_score(input, desc):
    value = input[desc]
    score = 0
    if (value != "") and (value != None):
        if value < 5000:
            score = 423
        elif value < 10000:
            score = 183
        elif value < 10500:
            score = 10
        elif value >= 10500:
            score = -126
    return score

# 7. INT_RATE
def retrieve_INT_RATE_score(input, desc):
    value = input[desc]
    score = 0
    if (value != "") and (value != None):
        if value < 8:
            score = 7
        elif value < 12:
            score = 3
        elif value < 15.5:
            score = 1
        elif value >= 15.5:
            score = -3
    return score

# 8. INSTALLMENT
def retrieve_INSTALLMENT_score(input, desc):
    value = input[desc]
    score = 0
    if (value != "") and (value != None):
        if value < 240:
            score = 75
        elif value < 880:
            score = -16
        elif value >= 880:
            score = -55
    return score

# 9. DTI
def retrieve_DTI_score(input, desc):
    value = input[desc]
    score = 0
    if (value != "") and (value != None):
        if value < 13:
            score = 16
        elif value < 21:
            score = 6
        elif value < 30:
            score = -9
        elif value >= 30:
            score = -25
    return score

# 10. INQ_LAST_6MTHS
def retrieve_INQ_LAST_6MTHS_score(input, desc):
    value = input[desc]
    score = 0
    if (value != "") and (value != None):
        if value < 1:
            score = 5
        elif value < 2:
            score = -3
        elif value < 3:
            score = -7
        elif value >= 3:
            score = -10
    return score

# 11. MTHS_SINCE_LAST_DELINQ
def retrieve_MTHS_SINCE_LAST_DELINQ_score(input, desc):
    value = input[desc]
    score = 0
    if (value != "") and (value != None):
        if (value == "") or (value == None):
            score = 1
        elif value < 8:
            score = -35
        elif value < 18:
            score = -21
        elif value >= 18:
            score = 9
    return score

# 12. MTHS_SINCE_LAST_RECORD
def retrieve_MTHS_SINCE_LAST_RECORD_score(input, desc):
    value = input[desc]
    score = 0
    if (value != "") and (value != None):
        if (value == "") or (value == None):
            score = -1
        elif value < 58:
            score = 1
        elif value < 80:
            score = 20
        elif value >= 80:
            score = -11
    return score

# 13. OPEN_ACC
def retrieve_OPEN_ACC_score(input, desc):
    value = input[desc]
    score = 0
    if (value != "") and (value != None):
        if value < 7:
            score = 3
        elif value < 8:
            score = -2
        elif value < 16:
            score = 1
        elif value < 21:
            score = -4
        elif value >= 21:
            score = -1
    return score

# 14. REVOL_UTIL
def retrieve_REVOL_UTIL_score(input, desc):
    value = input[desc]
    score = 0
    if (value != "") and (value != None):
        if (value == "") or (value == None):
            score = 2
        elif value < 30:
            score = 6
        elif value < 40:
            score = 3
        elif value < 55:
            score = 1
        elif value < 80:
            score = -2
        elif value >= 80:
            score = -7
    return score

# 15. TOTAL_ACC
def retrieve_TOTAL_ACC_score(input, desc):
    value = input[desc]
    score = 0
    if (value != "") and (value != None):
        if value < 10:
            score = -16
        elif value < 18:
            score = -6
        elif value < 28:
            score = -1
        elif value >= 28:
            score = 7
    return score

# 16. TOTAL_REC_PRNCP
def retrieve_TOTAL_REC_PRNCP_score(input, desc):
    value = input[desc]
    score = 0
    if (value != "") and (value != None):
        if value < 1000:
            score = -607
        elif value < 2000:
            score = -323
        elif value < 5000:
            score = -62
        elif value < 8500:
            score = 299
        elif value >= 8500:
            score = 658
    return score

# 17. TOTAL_REC_INT
def retrieve_TOTAL_REC_INT_score(input, desc):
    value = input[desc]
    score = 0
    if (value != "") and (value != None):
        if value < 200:
            score = 167
        elif value < 600:
            score = 39
        elif value < 1300:
            score = -58
        elif value >= 1300:
            score = -148
    return score

# 18. LAST_PYMNT_AMNT
def retrieve_LAST_PYMNT_AMNT_score(input, desc):
    value = input[desc]
    score = 0
    if (value != "") and (value != None):
        if value < 2000:
            score = -232
        elif value < 5000:
            score = 461
        elif value >= 5000:
            score = 568
    return score

# 19. MTHS_SINCE_LAST_MAJOR_DEROG
def retrieve_MTHS_SINCE_LAST_MAJOR_DEROG_score(input, desc):
    value = input[desc]
    score = 0
    if (value == "") or (value == None):
        score = 0
    elif value < 25:
        score = -12
    elif value < 40:
        score = 1
    elif value >= 40:
        score = 3
    return score

# 20. TOT_CUR_BAL
def retrieve_TOT_CUR_BAL_score(input, desc):
    value = input[desc]
    score = 0
    if (value != "") and (value != None):
        if value < 140000:
            score = -12
        elif value < 360000:
            score = 18
        elif value >= 360000:
            score = 39
    return score

# 21. TOTAL_REV_HI_LIM
def retrieve_TOTAL_REV_HI_LIM_score(input, desc):
    value = input[desc]
    score = 0
    if (value != "") and (value != None):
        if value < 6000:
            score = 18
        elif value < 18000:
            score = 6
        elif value < 38000:
            score = -1
        elif value < 80000:
            score = -9
        elif value >= 80000:
            score = -20
    return score