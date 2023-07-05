import streamlit as st
import io
import requests
import json

# Get the OpenAI API key from Streamlit secrets
api_key = st.secrets["openai_api_key"]

# Create the axios request
url = "https://api.openai.com/v1/engines/whisper/completions"
headers = {"Authorization": f"Bearer {api_key}"}
data = {"prompt": "Transcribe this audio file:"}

# Upload the audio file
file_upload = st.file_uploader("Upload Audio", type=["wav", "mp3", "m4a"])
if file_upload is not None:
    audio_file = file_upload.read()

    # Send the axios request
    response = requests.post(url, headers=headers, data=data, files={"file": audio_file})

    # Check the response status code
    if response.status_code == 200:
        # Get the transcription
        transcription = json.loads(response.content)["choices"][0]["text"]
        st.write(transcription)
    else:
        st.error("Error getting transcription")

