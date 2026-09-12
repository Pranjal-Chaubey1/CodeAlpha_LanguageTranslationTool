import io
import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS

# Configure Page UI
st.set_page_config(
    page_title="PolyGlot AI | Smart Translator",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom Aesthetic CSS
st.markdown("""
    <style>
    /* Main container styling */
    .stApp {
        background-color: #0F172A;
        color: #F8FAFC;
    }
    
    /* Header styling */
    .header-title {
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #6366F1 0%, #A855F7 50%, #EC4899 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.2rem;
    }
    .header-sub {
        text-align: center;
        color: #94A3B8;
        font-size: 1rem;
        margin-bottom: 2rem;
    }

    /* Input area styling */
    .stTextArea textarea {
        background-color: #1E293B !important;
        color: #F8FAFC !important;
        border: 1px solid #334155 !important;
        border-radius: 12px !important;
        font-size: 1rem !important;
    }
    .stTextArea textarea:focus {
        border-color: #6366F1 !important;
        box-shadow: 0 0 10px rgba(99, 102, 241, 0.3) !important;
    }

    /* Custom Select Boxes */
    .stSelectbox div[data-baseweb="select"] {
        background-color: #1E293B !important;
        border-radius: 10px !important;
        border: 1px solid #334155 !important;
    }

    /* Primary Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #6366F1 0%, #4F46E5 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.6rem 1rem !important;
        font-weight: 600 !important;
        font-size: 1.05rem !important;
        box-shadow: 0 4px 14px 0 rgba(99, 102, 241, 0.39) !important;
        transition: all 0.2s ease-in-out !important;
    }
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px 0 rgba(99, 102, 241, 0.5) !important;
    }

    /* Output Card */
    .result-card {
        background-color: #1E293B;
        border-left: 5px solid #A855F7;
        border-radius: 12px;
        padding: 1.2rem;
        margin-top: 1.5rem;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3);
    }
    .result-label {
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #A855F7;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .result-text {
        font-size: 1.15rem;
        color: #F8FAFC;
        line-height: 1.6;
    }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("<div class='header-title'>✨ PolyGlot AI</div>", unsafe_allow_html=True)
st.markdown("<div class='header-sub'>Instant neural translation powered by Cloud AI</div>", unsafe_allow_html=True)

# Languages Mapping
LANGUAGES = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Hindi": "hi",
    "Bengali": "bn",
    "Chinese (Simplified)": "zh-CN",
    "Japanese": "ja",
    "Arabic": "ar",
    "Russian": "ru",
    "Portuguese": "pt"
}

# Language Selectors Container
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        src_lang = st.selectbox("Source Language", list(LANGUAGES.keys()), index=0)
    with col2:
        tgt_lang = st.selectbox("Target Language", list(LANGUAGES.keys()), index=5)

# Text Input
input_text = st.text_area("Enter text to translate:", height=130, placeholder="Type your text here...")

# Translate Button Action
if st.button("Translate Text", use_container_width=True):
    if input_text.strip():
        try:
            with st.spinner("Translating..."):
                # AI Translation using Google Translate API
                translated_text = GoogleTranslator(
                    source=LANGUAGES[src_lang], 
                    target=LANGUAGES[tgt_lang]
                ).translate(input_text)

            # Output UI Box
            st.markdown(f"""
                <div class="result-card">
                    <div class="result-label">Translated Text ({tgt_lang})</div>
                    <div class="result-text">{translated_text}</div>
                </div>
            """, unsafe_allow_html=True)
            
            # Easy Copy Feature
            st.code(translated_text, language=None)

            # Text-to-Speech Output
            tts = gTTS(text=translated_text, lang=LANGUAGES[tgt_lang])
            fp = io.BytesIO()
            tts.write_to_fp(fp)
            st.audio(fp, format="audio/mp3")

        except Exception as e:
            st.error(f"Translation failed: {e}")
    else:
        st.warning("Please enter text to translate.")
