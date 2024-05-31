import streamlit as st
import openai
from pathlib import Path

# Function to convert text to speech
def text_to_speech(text, filename, voice="alloy"):
    openai.api_key = st.secrets["api_keys"]["openai"]
    response = openai.Audio.create(
        model="tts-1",
        voice=voice,
        input=text
    )
    with open(filename, 'wb') as audio_file:
        audio_file.write(response.audio_content)
    return filename

# Function to display story
def display_story(story):
    st.image(story['image'], use_column_width=True)
    st.subheader(story['title'])
    st.markdown(story['summary'])
    if st.button("Read Full Story", key=f"read_{story['id']}"):
        st.markdown(story['full_text'])
        audio_file = f"audio_{story['id']}.mp3"
        if st.button("Generate Audio", key=f"audio_{story['id']}"):
            with st.spinner('Generating audio...'):
                text_to_speech(story['full_text'], audio_file, "alloy")
            st.audio(audio_file, format='audio/mp3')
            with open(audio_file, "rb") as file:
                st.download_button(
                    label="Download MP3",
                    data=file,
                    file_name=audio_file,
                    mime="audio/mpeg"
                )
        if st.button("Copy Text", key=f"copy_{story['id']}"):
            st.write("Text Copied!")

# List of stories
stories = [
    {
        "id": "story1",
        "title": "The Unlikely Hero",
        "summary": "In a galaxy torn apart by war...",
        "full_text": "Full text of the story...",
        "image": "story-image1.png"
    },
    {
        "id": "story2",
        "title": "Echoes of the Future",
        "summary": "In the neon shadows of Neo-Tokyo...",
        "full_text": "Full text of the story...",
        "image": "story-image2.png"
    },
    # Add more stories here...
]

# Streamlit App Layout
st.title("Fast AI Fiction")
st.markdown("[Generate Audio 🔗](//tts-reader.streamlit.app/)", unsafe_allow_html=True)

st.markdown("## Stories")
for story in stories:
    display_story(story)

# Text-to-Speech Section
st.markdown("## Text-to-Speech")
st.subheader("Convert any text to speech using OpenAI's TTS Audio API. You can also download the result in .mp3 format.")
text = st.text_area("Enter the text you want to convert to speech:")
voice = st.selectbox("Choose a voice", ["alloy", "echo", "fable", "onyx", "nova", "shimmer"])

if st.button("Convert to Speech"):
    if text:
        with st.spinner('Generating audio...'):
            filename = "output.mp3"
            file_path = text_to_speech(text, filename, voice)
            st.audio(file_path, format='audio/mp3')
            with open(file_path, "rb") as file:
                st.download_button(
                    label="Download MP3",
                    data=file,
                    file_name=filename,
                    mime="audio/mpeg"
                )
    else:
        st.warning("Please enter some text to convert.")
