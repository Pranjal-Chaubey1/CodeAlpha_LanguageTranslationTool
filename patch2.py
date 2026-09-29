import re

with open("app.py", "r") as f:
    content = f.read()

content = content.replace("from deep_translator import GoogleTranslator", "from translate import Translator")

text_translation_old = """                    # AI Translation using Google Translate API
                    translated_text = GoogleTranslator(
                        source=LANGUAGES[src_lang], 
                        target=LANGUAGES[tgt_lang]
                    ).translate(input_text)"""

text_translation_new = """                    # AI Translation using translate library
                    translator = Translator(from_lang=LANGUAGES[src_lang], to_lang=LANGUAGES[tgt_lang])
                    translated_text = translator.translate(input_text)"""

content = content.replace(text_translation_old, text_translation_new)

doc_translation_old = """                        translator = GoogleTranslator(source=LANGUAGES[src_lang], target=LANGUAGES[tgt_lang])
                        # Use translate_batch as suggested by the error message to avoid rate limits
                        translated_chunks = translator.translate_batch(chunks)
                        translated_doc = "".join(translated_chunks)"""

doc_translation_new = """                        translator = Translator(from_lang=LANGUAGES[src_lang], to_lang=LANGUAGES[tgt_lang])
                        import time
                        translated_chunks = []
                        for chunk in chunks:
                            translated_chunks.append(translator.translate(chunk))
                            time.sleep(0.5)
                        translated_doc = "".join(translated_chunks)"""

content = content.replace(doc_translation_old, doc_translation_new)

# Also reduce the chunk size since translate uses a different API that might have smaller limits (500 is safe)
content = content.replace("chunks = textwrap.wrap(file_contents, width=4500, replace_whitespace=False)", "chunks = textwrap.wrap(file_contents, width=500, replace_whitespace=False)")

with open("app.py", "w") as f:
    f.write(content)
print("patched!")
