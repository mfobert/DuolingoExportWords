
source_lang = 'es'
dest_lang = 'en'

# This is a sample Python script.
import json
from googletrans import Translator

#JSON FILE FROM https://www.duolingo.com/vocabulary/overview

def parse_json(filename):
    #load file
    file = open(filename, "r")

    json_contents = file.read()

    json_parsed = json.loads(json_contents)

    word_json_objects = json_parsed['vocab_overview']
    words = []
    for word_json_object in word_json_objects:
        words.append(word_json_object['word_string'])

    words.sort()
    words = list(dict.fromkeys(words)) #remove duplicates


    translator = Translator()
    translations = translator.translate(words, src=source_lang, dest=dest_lang)
    for translation in translations:

        print(translation.origin , " , " , translation.text)


    file.close()


if __name__ == '__main__':
    parse_json('JSON_FILE_NAME.json')
