import streamlit as st
import json
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from templates import template_string
from helper import csv_to_string

st.title("MeetSync")

datacsv = st.file_uploader("Upload you Csv", type="csv")
if datacsv:
    load_dotenv()
    transcript = csv_to_string(datacsv)
    prompt_template = ChatPromptTemplate.from_template(template_string)
    action_items = prompt_template.format_messages(transcript = transcript)

    # Call ChatGPT to extract action items 
    chat = ChatOpenAI(temperature=0.0)
    action_str = chat(action_items)
    output_str = action_str.content
    action_dict = json.loads(output_str)
    st.write(action_dict)


