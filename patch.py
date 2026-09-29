import re

with open("app.py", "r") as f:
    content = f.read()

# Replace the single text input logic with tabs for text and file
text_to_replace = """# Text Input
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
            st.markdown(f\"\"\"
                <div class="result-card">
                    <div class="result-label">Translated Text ({tgt_lang})</div>
                    <div class="result-text">{translated_text}</div>
                </div>
            \"\"\", unsafe_allow_html=True)
            
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
        st.warning("Please enter text to translate.")"""

replacement_text = """# Tabs for Text and Document translation
tab1, tab2 = st.tabs(["Text Translation", "Document Translation"])

with tab1:
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
                st.markdown(f\"\"\"
                    <div class="result-card">
                        <div class="result-label">Translated Text ({tgt_lang})</div>
                        <div class="result-text">{translated_text}</div>
                    </div>
                \"\"\", unsafe_allow_html=True)
                
                # Easy Copy Feature
                st.code(translated_text, language=None)

                # Text-to-Speech Output
                tts = gTTS(text=translated_text, lang=LANGUAGES[tgt_lang])
                import io
                fp = io.BytesIO()
                tts.write_to_fp(fp)
                st.audio(fp, format="audio/mp3")

            except Exception as e:
                st.error(f"Translation failed: {e}")
        else:
            st.warning("Please enter text to translate.")

with tab2:
    uploaded_file = st.file_uploader("Upload a text file (.txt)", type=["txt"])
    if uploaded_file is not None:
        file_contents = uploaded_file.getvalue().decode("utf-8")
        st.text_area("Original File Content:", value=file_contents, height=130, disabled=True)
        
        if st.button("Translate Document", use_container_width=True):
            if file_contents.strip():
                try:
                    with st.spinner("Translating Document..."):
                        import textwrap
                        # Google Translate API has a 5000 character limit
                        chunks = textwrap.wrap(file_contents, width=4500, replace_whitespace=False)
                        
                        translator = GoogleTranslator(source=LANGUAGES[src_lang], target=LANGUAGES[tgt_lang])
                        translated_chunks = []
                        for chunk in chunks:
                            translated_chunks.append(translator.translate(chunk))
                        
                        translated_doc = "".join(translated_chunks)
                        
                    st.success("Translation Complete!")
                    st.download_button(
                        label="Download Translated File",
                        data=translated_doc,
                        file_name=f"translated_{tgt_lang}.txt",
                        mime="text/plain"
                    )
                except Exception as e:
                    st.error(f"Document translation failed: {e}")
            else:
                st.warning("The uploaded file is empty.")"""

if text_to_replace in content:
    with open("app.py", "w") as f:
        f.write(content.replace(text_to_replace, replacement_text))
    print("Successfully patched app.py")
else:
    print("Could not find the text to replace in app.py")
