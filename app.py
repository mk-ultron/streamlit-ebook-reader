import streamlit as st
import openai
from pathlib import Path

# Load the OpenAI API key from Streamlit's secrets
api_key = st.secrets["api_keys"]["openai"]

def text_to_speech(text, filename, voice="alloy"):
    # Initialize the OpenAI client with the API key
    openai.api_key = api_key
    client = openai.OpenAI(api_key=api_key)
    
    # Make a request to OpenAI's TTS API to convert text to speech
    response = client.audio.speech.create(
        model="tts-1",
        voice=voice,
        input=text
    )
    
    # Save the audio content to a file
    with open(filename, 'wb') as audio_file:
        audio_file.write(response.audio_content)
    return filename

# Function to display story
def display_story(story):
    col = st.columns(1)[0]
    with col:
        st.image(story['image'], use_column_width=True)
        st.subheader(story['title'])
        st.markdown(story['summary'])
        if st.button("Read Full Story", key=f"read_{story['id']}"):
            st.session_state[f"modal_{story['id']}"] = True

# Function to display modals for full stories
def display_modals(stories):
    for story in stories:
        if st.session_state.get(f"modal_{story['id']}", False):
            with st.modal(title=story['title']):
                st.image(story['image'], use_column_width=True)
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
                if st.button("Close", key=f"close_{story['id']}"):
                    st.session_state[f"modal_{story['id']}"] = False

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

# Custom CSS for responsive layout
st.markdown("""
    <style>
    .story-card {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-around;
    }
    .story-card > div {
        flex: 0 1 30%;
        margin: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Display stories
st.markdown('<div class="story-card">', unsafe_allow_html=True)
for story in stories:
    display_story(story)
st.markdown('</div>', unsafe_allow_html=True)

# Display modals
display_modals(stories)
