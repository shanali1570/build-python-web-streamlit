import streamlit as st
from googletrans import Translator

# Initialize the translator
translator = Translator()

# Title of the app
st.title("🌐 Language Translation App")

# Instructions for the user
st.write("""
Enter text in one language, select the target language, and get the translation instantly!
""")

# Text Input
user_input = st.text_area("Enter text to translate:", height=100)

# Language Selection (Updated to include Urdu)
languages = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Chinese (Simplified)": "zh-cn",
    "Japanese": "ja",
    "Korean": "ko",
    "Hindi": "hi",
    "Urdu": "ur",
}

source_lang = st.selectbox("Select source language:", list(languages.keys()))
target_lang = st.selectbox("Select target language:", list(languages.keys()))

# Translate Button
if st.button("Translate"):
    if user_input.strip() == "":
        st.error("Please enter some text to translate.")
    elif source_lang == target_lang:
        st.error("Source and target languages cannot be the same.")
    else:
        # Perform translation
        try:
            translated = translator.translate(
                user_input, src=languages[source_lang], dest=languages[target_lang]
            )
            st.subheader("Translated Text")
            st.success(translated.text)
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Footer
st.write("---")
st.write("Created with ❤️ Syed Muhammad Shan-e-Ali")