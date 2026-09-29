# AI Language Translation Tool 🌐

This project is **Task 1** for the **CodeAlpha Artificial Intelligence Internship**. 

It is a lightweight web application that allows users to enter text, select source and target languages, and receive accurate translations using an AI-powered translation API. It also includes an optional Text-to-Speech feature for better usability.

## Features
- **Multi-Language Support**: Translates between multiple major global languages.
- **AI Translation API**: Utilizes the `translate` library for fast and accurate results.
- **Document Translation**: Allows uploading a text file (`.txt`) and translating its entire content.
- **Text-to-Speech (TTS)**: Converts the translated text into playable audio using `gTTS`.
- **Aesthetic UI**: Built using Streamlit for a clean, responsive, and easy-to-use interface.

## Tech Stack
- Python 3
- Streamlit (Frontend)
- translate (AI Translation)
- gTTS (Audio Output)

## How to Run Locally
Follow these exact steps to start the application:

1. **Open a terminal** and navigate to the project directory:
   ```bash
   cd CodeAlpha_LanguageTranslationTool
   ```
2. **Create a virtual environment** (optional but recommended):
   ```bash
   python3 -m venv venv
   ```
3. **Activate the virtual environment**:
   - On Linux/macOS:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\\Scripts\\activate
     ```
4. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
5. **Run the Streamlit application**:
   ```bash
   streamlit run app.py
   ```
6. **Open your browser** and navigate to the provided local URL (usually `http://localhost:8501`).
