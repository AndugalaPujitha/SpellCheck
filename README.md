# Spelling Checker [  🌐Demo](https://spellcheckersystem.streamlit.app/)

Introduction:
This Python application allows users to check the spelling of words entered into the text entry field. It provides suggestions for correctly spelled words and displays synonyms for the suggested word. The graphical user interface (GUI) is implemented using the Tkinter library, and the spelling check functionality is powered by the TextBlob library and NLTK's WordNet.

Requirements:
- Python 3.x
- Tkinter
- TextBlob
- NLTK (including the WordNet corpus)
- PIL (Python Imaging Library)
- requests

Installation:
Ensure you have Python installed on your system. You can install the required Python libraries using pip:

pip install tk textblob nltk pillow

For NLTK, download the WordNet corpus by running the following Python commands:

import nltk
nltk.download('wordnet')

Features:
- Users can input words for spelling correction.
- The application suggests the corrected spelling of the word.
- It provides synonyms for the corrected word.
- The background of the GUI is dynamically set using an image fetched from a URL.

Acknowledgments:
- This application utilizes the Tkinter library for GUI development and TextBlob for spelling correction.
- Credits to NLTK for providing the WordNet corpus for synonym retrieval.
- Special thanks to the developers of PIL (Python Imaging Library) for image processing capabilities.
