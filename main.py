import streamlit as st
import openai
import os

# Retrieve API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def main():
    st.title("Audio Transcription with OpenAI")
    
    # Upload audio file
    audio_file = st.file_uploader("Upload audio file", type=["mp3", "wav"])
    
    if audio_file is not None:
        # Transcribe audio
        st.text("Transcribing audio...")
        transcript = transcribe_audio(audio_file)
        
        # Display the transcript
        st.text_area("Transcript", transcript)
    
    else:
        st.warning("Please upload an audio file.")

def transcribe_audio(audio_file):
    try:
        # Read audio file content
        audio_content = audio_file.read()
        
        # Call OpenAI API to transcribe the audio
        response = openai.Audio.transcribe("whisper-1", audio_content)
        
        # Get the transcript
        transcript = response['transcriptions'][0]['text']
        
        return transcript
    
    except Exception as e:
        st.error(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    main()

