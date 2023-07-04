import streamlit as st
import openai

# Retrieve the API key from Streamlit secrets
api_key = st.secrets["api_key"]

# Initialize the OpenAI API client
openai.api_key = api_key

# Streamlit app code
def main():
    st.title("Audio Transcription")

    # File uploader
    audio_file = st.file_uploader("Upload an audio file", type=["mp3", "wav"])

    if audio_file is not None:
        # Convert audio to text
        transcript = transcribe_audio(audio_file)
        st.header("Transcript")
        st.write(transcript)

def transcribe_audio(audio_file):
    # Convert audio to text using the OpenAI API
    response = openai.Audio.transcribe("whisper-1", audio_file)
    return response["transcriptions"][0]["transcript"]

if __name__ == "__main__":
    main()
  
