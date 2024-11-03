from deep_translator import GoogleTranslator

def translate_file(input_file, output_file, target_language):
    # Create a GoogleTranslator object
    translator = GoogleTranslator(target=target_language)

    # Read the contents of the input file
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Translate the text to the target language
    translated_text = translator.translate(text)

    # Write the translated text to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(translated_text)

    print(f"Translation completed and saved to {output_file}")

if __name__ == '__main__':
    input_file = 'extraction_and_submitting.py'   # Replace with your input .txt file
    output_file = 'translated_output.py'  # The file where translated text will be saved
    target_language = 'ja'  # Replace with the desired language code (e.g., 'fr' for French, 'es' for Spanish)

    translate_file(input_file, output_file, target_language)
