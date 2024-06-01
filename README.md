# Streamlit eBook Reader

Welcome to the Streamlit eBook Reader! This project is a Streamlit application that allows users to read and listen to short stories. The stories can be viewed with images, summaries, and full text, and users can generate audio versions of the stories using OpenAI's Text-to-Speech (TTS) API.

## Features

- Display stories with images, titles, and summaries.
- Expand to read the full text of each story.
- Generate and listen to audio versions of the full stories.
- Download the generated audio files in MP3 format.

## Demo

Check out the live demo of the app: [Streamlit eBook Reader](https://ebook-reader.streamlit.app/)

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/mk-ultron/streamlit-ebook-reader.git
    cd streamlit-ebook-reader
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up Streamlit secrets for OpenAI API key:
    - Create a file named `secrets.toml` in the `.streamlit` directory:
      ```toml
      [api_keys]
      openai = "your_openai_api_key"
      ```

5. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## Usage

After running the Streamlit app, you can open your browser and navigate to `http://localhost:8501` to view and interact with the eBook Reader.

## Project Structure

- `app.py`: The main application file containing the Streamlit code.
- `requirements.txt`: The list of dependencies required to run the project.
- `.streamlit/secrets.toml`: Configuration file for storing secrets (e.g., OpenAI API key).

## Code Overview

### app.py

- **Imports and Configuration**:
  - Imports necessary libraries and sets up the Streamlit page configuration.
  - Loads the OpenAI API key from Streamlit's secrets.

- **text_to_speech Function**:
  - Converts text to speech using OpenAI's TTS API and saves the audio content to a file.

- **display_story Function**:
  - Displays a story with its image, title, summary, and full text.
  - Provides a button to generate and play the audio version of the story and a button to download the audio file.

- **format_full_text Function**:
  - Formats the full text of the story by wrapping paragraphs in HTML `<p>` tags.

- **Stories List**:
  - Contains details of the stories to be displayed, including IDs, titles, summaries, full texts, and images.

- **Streamlit App Layout**:
  - Sets up the layout of the Streamlit app, including custom CSS for responsive design.
  - Displays stories in a grid layout using Streamlit columns.

## Acknowledgements

- [Streamlit](https://streamlit.io/) for providing an awesome framework to create interactive web applications.
- [OpenAI](https://openai.com/) for the powerful Text-to-Speech API.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue if you have any suggestions or improvements.
---

Happy reading and listening!
```

Note: Make sure to replace `"your_openai_api_key"` with your own OpenAI API key.
