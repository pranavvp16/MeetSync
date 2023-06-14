import streamlit as st
import os 
import csv
import json
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from templates import template_string


def csv_to_string(file):
    next(file)
    combined_string = ""
    # Iterate over each row in the CSV file
    for row in file:
        # Extract the values from the row
        time_start = row[0]
        time_end = row[1]
        text = row[2]
        action = row[3]

        # Concatenate the values in the desired format
        combined_string += f"{time_start}-{time_end} : {text} : {action}\n"
    return combined_string

st.title("MeetSync")

datacsv = st.file_uploader("Upload you Csv", type="csv")
data_str = csv_to_string(datacsv)

transcript = template_string
prompt_template = ChatPromptTemplate.from_template(template_string)
action_items = prompt_template.format_messages(transcript = transcript)

# Call ChatGPT to extract action items 
chat = ChatOpenAI(temperature=0.0)
action_str = chat(action_items)


