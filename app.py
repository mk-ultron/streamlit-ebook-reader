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
# Streamlit App Layout
st.title("Fast AI Fiction")

st.markdown("## Stories")
for story in stories:
    display_story(story)


# List of stories
stories = [
    {
        "id": "story1",
        "title": "The Unlikely Hero",
        "summary": "In a galaxy torn apart by war, a humble mechanic named Kira discovers a dying prince and a secret that could unite the warring factions against an ancient, unstoppable force. Embark on an interstellar journey of courage and hope as Kira rises to become the hero the galaxy never expected.",
        "full_text": "The galaxy was at war. Starfleets clashed in the cold void, planets burned, and alliances crumbled. Amidst this chaos, Kira, a lowly mechanic on the barren moon of Kestris, found herself thrust into the heart of the conflict. She had always believed her life would be spent repairing starships and dreaming of adventure, but fate had other plans.

One fateful day, while scavenging for parts, Kira stumbled upon a crashed escape pod. Inside was a gravely injured alien who identified himself as Prince Thallan, heir to the Throne of Arion, a planet key to the balance of power in the galaxy. The prince carried a message of a greater threat—an ancient, malevolent force from beyond the stars, known as the Voidbringers, poised to conquer and consume all in their path.

With his dying breath, Prince Thallan entrusted Kira with a data crystal containing vital information that could unite the warring factions against the Voidbringers. Kira, never one to shirk from a challenge, vowed to honor the prince's last wish. She repaired a derelict starfighter, took the crystal, and embarked on a perilous journey.

Her path was fraught with danger—she faced hostile patrols, treacherous smugglers, and the ever-looming threat of the Voidbringers. Along the way, she forged unlikely alliances with rebels, outlaws, and soldiers from enemy planets. Kira's courage and determination inspired those she met, and her mission quickly became a beacon of hope.

In the climactic battle, as the Voidbringers descended upon the galaxy, Kira's ragtag fleet, now united, launched a desperate defense. With the help of the data crystal, they discovered the Voidbringers' weakness and struck a decisive blow. The galaxy, though scarred by war, was saved.

Kira, the mechanic turned hero, had done the impossible. She had united the galaxy and defeated the greatest threat it had ever faced. The war ended, and peace, though fragile, began to bloom. Kira returned to Kestris, but her name would forever be remembered among the stars.",
        "image": "story-image1.png"
    },
    {
        "id": "story2",
        "title": "Echoes of the Future",
        "summary": "In the neon shadows of Neo-Tokyo...",
        "full_text": "In the neon-lit sprawl of Neo-Tokyo, the line between the virtual and real world had long since blurred. Megacorporations ruled with iron fists, and the city thrummed with the hum of technology and the whispers of dissent. Amidst this dystopian landscape, Jax, a rogue hacker known for his skill and audacity, stumbled upon a conspiracy that could change everything.

Jax had always worked alone, his only companions the countless data streams and the cold glow of his multiple monitors. One night, while navigating the dark web, he intercepted an encrypted message hinting at a project called "Echoes"—a secret program designed to control and manipulate human consciousness within the virtual world.

Determined to uncover the truth, Jax infiltrated the most secure servers of the megacorporation CyberDyne. What he found chilled him to the bone. Echoes was not just a project; it was a reality. CyberDyne had developed a technology capable of rewriting memories and altering perceptions, effectively controlling the populace by manipulating their minds in both the virtual and physical worlds.

Realizing the implications, Jax knew he couldn't fight this battle alone. He reached out to an underground network of hackers and cyber-activists. Together, they devised a plan to expose CyberDyne's treachery. The mission was perilous, but the stakes were too high to ignore.

As Jax and his allies launched their cyber-assault, CyberDyne's defenses retaliated with ruthless efficiency. The battle raged in cyberspace, codes clashing like digital titans. Just when all seemed lost, Jax managed to upload the incriminating data to every major network, ensuring that the truth could not be suppressed.

The world watched in shock as the extent of CyberDyne's manipulation was unveiled. Protests erupted, and the megacorporation's power crumbled under the weight of public outrage. In the aftermath, new regulations were put in place to prevent such abuse of technology.

Jax, though a shadow in the digital world, had become a beacon of hope. He continued to fight for freedom in the ever-evolving virtual landscape, knowing that the battle for humanity's soul was far from over.",
        "image": "story-image2.png"
    },
    
]


