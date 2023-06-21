# 🦜⛓️ MeetSync
In today's fast-paced world, effective communication and collaboration are crucial for successful project management. Meetings play a vital role in fostering teamwork and exchanging valuable information. However, keeping track of action items and important tasks discussed during meetings can be challenging and time-consuming. That's where MeetSync comes in.

MeetSync is a project developed using the Langchain framework and powered by OpenAI GPT-3.5 turbo language model. Its primary objective is to streamline the process of extracting action items from video transcripts, making it easier than ever to capture and organize crucial tasks assigned during meetings.

## Setup the Codebase
The repository that contains the project is : [Project](https://github.com/pranavvp16/MeetSync)<br>

### Cloning repository locally
```bash
git clone https://github.com/pranavvp16/MeetSync.git
```

### Install dependancies 
It's better to install this dependancies in pyvenv or conda environment with python>=3.8<br>
```bash
pip install -r requirements.txt
```

### Set up environment variables 
Create a `.env` file and save the openAI key in it.<br>
```
OPENAI_API_KEY = <your_api_key>
```

### Running the streamlit server
Run the streamlit server.
```bash
streamlit run app.py
```

### Extracting action items
Upload a transcript csv from `MeetSync/data` to run the code(pipeline) that finds action items from the transcript.