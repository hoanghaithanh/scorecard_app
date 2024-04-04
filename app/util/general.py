import json
import streamlit as st
import pandas as pd
import numpy as np

def load_input(input_path="./input/input.json"):
    # load input file
    with open(input_path, "r") as file:
        input = json.load(file)
    print(input["Interest Rate on the loan"])
    return input

def save_input(input, input_path="./input/input.json"):
    # save input file
    with open(input_path, "w") as file:
        json.dump(input, file)
    print("Input was saved successfully")

def convert_to_INT(value):
    # convert input value to integer
    try:
        value = int(value)
        if value >= 0:
            return value
        else:
            st.error("This cell only accept POSITIVE value.", icon="🚨")
    except:
        if (value != "") and value:
            st.error("This cell only accept INTEGER value.", icon="🚨")

def convert_to_FLOAT(value):
    # convert input value to integer
    try:
        value = float(value)
        if value >= 0:
            return value
        else:
            st.error("This cell only accept POSITIVE value.", icon="🚨")
    except:
        if (value != "") and value:
            st.error("This cell only accept FLOAT value.", icon="🚨")

def find_index(value, options):
    # find index in options list for declared value
    index = None
    for i in range(len(options)):
        if value == options[i]:
            index = i
    return index

def retrieve_min_max_credit_score(base_score, scorecard_path="./scorecard/2024-02-11_Scorecard_Basepoints_452.csv"):
    # calculate possible min, max credit score
    scorecard = pd.read_csv(scorecard_path)
    features = np.unique(scorecard['variable'])
    min_score, max_score = base_score, base_score
    for feature in features:
        points = list(scorecard[scorecard['variable'] == feature]['points'])
        min_point = min(points)
        max_point = max(points)
        if min_point < 0:
            min_score += min_point
        if max_point > 0:
            max_score += max_point
    return min_score, max_score
