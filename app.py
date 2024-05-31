import streamlit as st
import openai
from pathlib import Path

# Function to convert text to speech
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
    speech_file_path = Path(filename)
    response.stream_to_file(speech_file_path)
    
    return filename

# Text-to-Speech Section
st.markdown("## Text-to-Speech")
st.subheader("Convert any of the story texts below to speech by copying the text and clicking convert. You can also download the result in .mp3 format.")
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
        
# Function to display story
def display_story(story):
    col = st.columns(1)[0]
    with col:
        st.image(story['image'], use_column_width=True)
        st.subheader(story['title'])
        st.markdown(story['summary'])
        with st.expander("Read Full Story"):
            st.markdown(format_full_text(story['full_text']), unsafe_allow_html=True)
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

# Function to format the full text of the story
def format_full_text(full_text):
    paragraphs = full_text.split("\n\n")
    formatted_text = "".join([f"<p>{paragraph}</p>" for paragraph in paragraphs])
    return formatted_text

# List of stories
stories = [
    {
        "id": "story1",
        "title": "The Unlikely Hero",
        "summary": "In a galaxy torn apart by war...",
        "full_text": """The galaxy was at war. Starfleets clashed in the cold void, planets burned, and alliances crumbled. Amidst this chaos, Kira, a lowly mechanic on the barren moon of Kestris, found herself thrust into the heart of the conflict. She had always believed her life would be spent repairing starships and dreaming of adventure, but fate had other plans.\n\nOne fateful day, while scavenging for parts, Kira stumbled upon a crashed escape pod. Inside was a gravely injured alien who identified himself as Prince Thallan, heir to the Throne of Arion, a planet key to the balance of power in the galaxy. The prince carried a message of a greater threat—an ancient, malevolent force from beyond the stars, known as the Voidbringers, poised to conquer and consume all in their path.\n\nWith his dying breath, Prince Thallan entrusted Kira with a data crystal containing vital information that could unite the warring factions against the Voidbringers. Kira, never one to shirk from a challenge, vowed to honor the prince's last wish. She repaired a derelict starfighter, took the crystal, and embarked on a perilous journey.""",
        "image": "story-image1.png"
    },
    {
        "id": "story2",
        "title": "Echoes of the Future",
        "summary": "In the neon shadows of Neo-Tokyo...",
        "full_text": """In the neon-lit sprawl of Neo-Tokyo, the line between the virtual and real world had long since blurred. Megacorporations ruled with iron fists, and the city thrummed with the hum of technology and the whispers of dissent. Amidst this dystopian landscape, Jax, a rogue hacker known for his skill and audacity, stumbled upon a conspiracy that could change everything.\n\nJax had always worked alone, his only companions the countless data streams and the cold glow of his multiple monitors. One night, while navigating the dark web, he intercepted an encrypted message hinting at a project called "Echoes"—a secret program designed to control and manipulate human consciousness within the virtual world.""",
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



