# AI Language Translation Tool 🌐

This project is **Task 1** for the **CodeAlpha Artificial Intelligence Internship**. 

It is a lightweight web application that allows users to enter text, select source and target languages, and receive accurate translations using an AI-powered translation API. It also includes an optional Text-to-Speech feature for better usability.

## Features
- **Multi-Language Support**: Translates between multiple major global languages.
- **AI Translation API**: Utilizes Google Translate via `deep-translator` for fast and accurate results.
- **Text-to-Speech (TTS)**: Converts the translated text into playable audio using `gTTS`.
- **Aesthetic UI**: Built using Streamlit for a clean, responsive, and easy-to-use interface.

## Tech Stack
- Python 3
- Streamlit (Frontend)
- deep-translator (AI Translation)
- gTTS (Audio Output)

## How to Run Locally
1. Clone the repository to your local machine.
2. Create and activate a Python virtual environment (`python3 -m venv venv` and `source venv/bin/activate`).
3. Install the dependencies: `pip install -r requirements.txt`.
4. Run the app: `streamlit run app.py`.
