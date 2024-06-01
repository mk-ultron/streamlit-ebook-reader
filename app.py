import streamlit as st
import openai
from pathlib import Path

st.set_page_config(layout="wide")

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
    speech_file_path = Path(filename)
    with open(speech_file_path, 'wb') as audio_file:
        audio_file.write(response["audio_content"])
    
    return filename
      
# Function to display story
def display_story(story, col):
    with col:
        st.markdown(f"""
            <div class="story-container">
                <img src="{story['image']}" class="story-image" />
                <h2>{story['title']}</h2>
                <p>{story['summary']}</p>
            </div>
        """, unsafe_allow_html=True)
        
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
        "summary": "In a galaxy torn apart by war, a humble mechanic named Kira discovers a dying prince and a secret that could unite the warring factions against an ancient, unstoppable force. Embark on an interstellar journey of courage and hope as Kira rises to become the hero the galaxy never expected.",
        "full_text": """The galaxy was at war. Starfleets clashed in the cold void, planets burned, and alliances crumbled. Amidst this chaos, Kira, a lowly mechanic on the barren moon of Kestris, found herself thrust into the heart of the conflict. She had always believed her life would be spent repairing starships and dreaming of adventure, but fate had other plans.\n\nOne fateful day, while scavenging for parts, Kira stumbled upon a crashed escape pod. Inside was a gravely injured alien who identified himself as Prince Thallan, heir to the Throne of Arion, a planet key to the balance of power in the galaxy. The prince carried a message of a greater threat—an ancient, malevolent force from beyond the stars, known as the Voidbringers, poised to conquer and consume all in their path.\n\nWith his dying breath, Prince Thallan entrusted Kira with a data crystal containing vital information that could unite the warring factions against the Voidbringers. Kira, never one to shirk from a challenge, vowed to honor the prince's last wish. She repaired a derelict starfighter, took the crystal, and embarked on a perilous journey.\n\nHer path was fraught with danger—she faced hostile patrols, treacherous smugglers, and the ever-looming threat of the Voidbringers. Along the way, she forged unlikely alliances with rebels, outlaws, and soldiers from enemy planets. Kira's courage and determination inspired those she met, and her mission quickly became a beacon of hope.\n\nIn the climactic battle, as the Voidbringers descended upon the galaxy, Kira's ragtag fleet, now united, launched a desperate defense. With the help of the data crystal, they discovered the Voidbringers' weakness and struck a decisive blow. The galaxy, though scarred by war, was saved.\n\nKira, the mechanic turned hero, had done the impossible. She had united the galaxy and defeated the greatest threat it had ever faced. The war ended, and peace, though fragile, began to bloom. Kira returned to Kestris, but her name would forever be remembered among the stars.""",
        "image": "story-image1.png"
    },
    {
        "id": "story2",
        "title": "Echoes of the Future",
        "summary": "In the neon shadows of Neo-Tokyo, rogue hacker Jax stumbles upon a chilling conspiracy that threatens both the virtual and real worlds. Join Jax on a high-stakes cyber adventure as he battles megacorporations to expose a sinister plot that could redefine humanity’s future.",
        "full_text": """In the neon-lit sprawl of Neo-Tokyo, the line between the virtual and real world had long since blurred. Megacorporations ruled with iron fists, and the city thrummed with the hum of technology and the whispers of dissent. Amidst this dystopian landscape, Jax, a rogue hacker known for his skill and audacity, stumbled upon a conspiracy that could change everything.\n\nJax had always worked alone, his only companions the countless data streams and the cold glow of his multiple monitors. One night, while navigating the dark web, he intercepted an encrypted message hinting at a project called "Echoes"—a secret program designed to control and manipulate human consciousness within the virtual world.\n\nDetermined to uncover the truth, Jax infiltrated the most secure servers of the megacorporation CyberDyne. What he found chilled him to the bone. Echoes was not just a project; it was a reality. CyberDyne had developed a technology capable of rewriting memories and altering perceptions, effectively controlling the populace by manipulating their minds in both the virtual and physical worlds.\n\nRealizing the implications, Jax knew he couldn't fight this battle alone. He reached out to an underground network of hackers and cyber-activists. Together, they devised a plan to expose CyberDyne's treachery. The mission was perilous, but the stakes were too high to ignore.\n\nAs Jax and his allies launched their cyber-assault, CyberDyne's defenses retaliated with ruthless efficiency. The battle raged in cyberspace, codes clashing like digital titans. Just when all seemed lost, Jax managed to upload the incriminating data to every major network, ensuring that the truth could not be suppressed.\n\nThe world watched in shock as the extent of CyberDyne's manipulation was unveiled. Protests erupted, and the megacorporation's power crumbled under the weight of public outrage. In the aftermath, new regulations were put in place to prevent such abuse of technology.\n\nJax, though a shadow in the digital world, had become a beacon of hope. He continued to fight for freedom in the ever-evolving virtual landscape, knowing that the battle for humanity's soul was far from over.""",
        "image": "story-image2.png"
    },
    {
        "id": "story3",
        "title": "The Clockwork Quest",
        "summary": "In the steam-powered city of Gearford, young inventor Elara and daring airship captain Gideon embark on a thrilling quest to uncover ancient technology. Explore a world of airships and clockwork wonders as they race against time to unlock the secrets of the lost city of Astralium.",
        "full_text": """In the steam-powered city of Gearford, where airships soared through smog-filled skies and clockwork mechanisms whirred tirelessly, young inventor Elara dreamed of discovery. Her life changed when she stumbled upon an ancient, forgotten map hidden within the gears of an old automaton.\n\nThe map led to the lost city of Astralium, rumored to house technology far beyond their own. Elara knew she couldn't embark on this journey alone, so she sought the help of Captain Gideon, a daring airship pilot known for his unorthodox methods and unmatched skills.\n\nTogether, they gathered a crew of misfits and set sail on the airship Aurora. Their quest was fraught with peril—treacherous skies, mechanical beasts, and rival treasure hunters. But Elara's ingenuity and Gideon's expertise saw them through each challenge.\n\nAs they delved deeper into uncharted territories, they uncovered clues about Astralium's secrets. The lost city was said to be powered by a core of pure aetherium, a substance with limitless energy potential. Such power could revolutionize their world, but in the wrong hands, it could spell disaster.\n\nAfter weeks of searching, they finally reached the hidden entrance to Astralium. Inside, they found wonders beyond imagination—machines that defied the laws of physics and constructs that seemed almost alive. But they also discovered the truth: the city's downfall had been caused by the very power it sought to harness.\n\nRealizing the dangers, Elara and Gideon decided to secure the knowledge and prevent it from falling into the wrong hands. They documented their findings, disabling the most dangerous devices, and sealed the city's entrance.\n\nReturning to Gearford, they shared their discoveries, advocating for responsible use of technology. Elara's reputation as an inventor soared, and Gideon became a legend. Together, they inspired a new era of innovation tempered with caution, ensuring the mistakes of Astralium would never be repeated.""",
        "image": "story-image3.png"
    },
    {
        "id": "story4",
        "title": "The Hidden Underworld",
        "summary": "Detective Lila Blake navigates the hidden underworld of New Avalon, where magical creatures and wizards dwell alongside humans. When a series of magical crimes threaten to unravel the city's delicate balance, Lila must bridge two worlds to uncover the truth and save her city from chaos.",
        "full_text": """In the bustling metropolis of New Avalon, Detective Lila Blake was known for her sharp mind and unyielding determination. However, few knew that Lila had a secret—she was one of the few humans aware of the city's hidden underworld, a realm of magical creatures and ancient wizards existing alongside the mundane world.\n\nHer dual knowledge came into play when a series of bizarre crimes began to plague New Avalon. Victims were found with strange, arcane symbols etched into their skin, and the air was thick with dark magic. Lila knew this wasn't the work of any ordinary criminal.\n\nUsing her connections in both worlds, Lila began her investigation. She consulted with Finn, a centuries-old wizard, and Delilah, a shapeshifter with a penchant for secrets. Together, they uncovered a sinister plot orchestrated by a rogue mage seeking to merge the magical and human realms by breaking the ancient barriers that separated them.\n\nAs the crimes escalated, Lila's two worlds collided. She had to navigate treacherous alliances and fend off magical attacks, all while keeping the truth hidden from her colleagues in the police force. The stakes were raised when the rogue mage kidnapped Delilah, intending to use her unique abilities to finalize the ritual.\n\nIn a race against time, Lila and Finn confronted the rogue mage in an abandoned cathedral, the epicenter of magical convergence. The battle was fierce, spells clashing and energy crackling in the air. Just as the mage began the final incantation, Lila, using a combination of wit and courage, disrupted the ritual, freeing Delilah and neutralizing the mage.\n\nWith the threat averted, the barriers between the worlds remained intact. Lila ensured the rogue mage was imprisoned in the magical realm, unable to threaten either world again. Her actions earned her respect in both realms, but she knew her work was far from over.\n\nNew Avalon thrived, with its secret underworld continuing to coexist in the shadows. And Detective Lila Blake stood as its silent guardian, ever vigilant against the dark forces that threatened the delicate balance.""",
        "image": "story-image4.png"
    },
    {
        "id": "story5",
        "title": "The Quest for the Crystal",
        "summary": "In the realm of Eldoria, darkness rises as the Dark Sorcerer Malakar seeks to conquer the land. A valiant knight, a skilled archer, a cunning rogue, and a young mage band together on a perilous quest for the legendary Crystal of Light. Witness their epic journey to save their world from eternal night.",
        "full_text": """In the ancient realm of Eldoria, where dragons soared through the skies and mythical creatures roamed the forests, a shadow of darkness began to spread. The Dark Sorcerer, Malakar, had risen, seeking to plunge the land into eternal night. The only hope lay in the legendary Crystal of Light, hidden deep within the heart of the Forbidden Mountain.A prophecy foretold that only a band of true-hearted adventurers could retrieve the crystal and save Eldoria. Thus, a diverse group was assembled: Eamon, a valiant knight; Lyra, a skilled archer; Thorne, a cunning rogue; and Arin, a young mage with untapped potential.\n\nTheir journey was fraught with peril. They crossed treacherous landscapes, battled fierce creatures, and solved ancient riddles. Along the way, they forged an unbreakable bond, each bringing their unique strengths to the fore. Eamon's bravery, Lyra's precision, Thorne's agility, and Arin's growing magical prowess complemented each other perfectly.\n\nAs they neared the Forbidden Mountain, Malakar's minions attacked in full force. The adventurers fought valiantly, but the dark magic was overwhelming. In a moment of desperation, Arin tapped into a hidden well of power, casting a spell that drove the minions back and revealed the entrance to the mountain.\n\nInside, they faced the final challenge: a labyrinth filled with traps and illusions. Their unity and trust in each other saw them through, leading them to the chamber of the Crystal of Light. As they approached, Malakar himself appeared, wielding dark sorcery.\n\nThe battle was fierce, with the very fate of Eldoria hanging in the balance. Just when all seemed lost, Eamon's courage, Lyra's arrows, Thorne's stealth, and Arin's magic combined in a final, desperate strike. The crystal unleashed a blinding light, vanquishing Malakar and dispelling the darkness.\n\nWith the Dark Sorcerer defeated, the realm of Eldoria was saved. The adventurers returned as heroes, their names forever etched in legend. The Crystal of Light was placed in the capital, a symbol of hope and unity.\n\nEldoria flourished, and the bond between the adventurers remained strong. They had not only saved their world but also proven that even in the darkest times, light and unity could prevail.""",
        "image": "story-image5.png"
    },
]

# Custom CSS for image centering and sizing
st.markdown("""
    <style>
    .story-container {
        text-align: center;
    }
    .story-image {
        max-width: 100%;
        height: auto;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
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

# Streamlit App Layout
st.title("Fast AI Fiction")

# Display stories
st.markdown('<div class="story-card">', unsafe_allow_html=True)
columns = st.columns(3)  # Create 3 columns

for i, story in enumerate(stories):
    display_story(story, columns[i % 3])  # Display each story in one of the 3 columns

st.markdown('</div>', unsafe_allow_html=True)



