import streamlit as st
from textblob import TextBlob
import nltk
from nltk.corpus import wordnet

# Download necessary data
nltk.download('wordnet')

# Function to get synonyms
def get_synonyms(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonym = lemma.name().replace("_", " ")
            synonyms.append(synonym)
    return list(set(synonyms))[:5]

# Set page config
st.set_page_config(page_title="Spell Checker", page_icon="✅", layout="centered")

# Background Styling
st.markdown(
    """
    <style>
    body {
        background-color: #f4f4f4;
        color: black;
    }
    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: white;
        background: black;
        padding: 10px;
        border-radius: 10px;
    }
    # .container {
    #     text-align: center;
    #     padding: 20px;
    #     background: white;
    #     border-radius: 10px;
    #     box-shadow: 0px 4px 8px rgba(0,0,0,0.2);
    #     width: 60%;
    #     margin: auto;
    # }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown('<div class="title">🔍 Spell Checker & Synonyms Finder</div>', unsafe_allow_html=True)
st.write("\n")  # Spacing

# Input Section
st.markdown('<div class="container">', unsafe_allow_html=True)
word = st.text_input("Type a word:", "", help="Enter a word to check its spelling.")

if word:
    corrected_word = str(TextBlob(word).correct())
    synonyms = get_synonyms(corrected_word)

    # Display results in a formatted container
    st.markdown(f"### ✅ Correct Spelling: **{corrected_word}**")
    
    if synonyms:
        st.markdown("### 🔄 Synonyms:")
        st.write(", ".join(synonyms))
    else:
        st.write("No synonyms found.")

st.markdown('</div>', unsafe_allow_html=True)
