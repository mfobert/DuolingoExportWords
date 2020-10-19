
source_lang = 'es'
dest_lang = 'en'
PATH_TO_JSON_FILE = 'PATH_TO_JSON_FILE.json' #JSON FILE FROM https://www.duolingo.com/vocabulary/overview  (JSON tab -> Save)

import json
from googletrans import Translator #pip install googletrans

def parse_json_and_print_translations(filename):
    #open and parse
    file = open(filename, "r")
    json_contents = file.read()
    json_parsed = json.loads(json_contents)
    word_json_objects = json_parsed['vocab_overview']
    words = []
    for word_json_object in word_json_objects:
        words.append(word_json_object['word_string'])
    
    #sort and filter
    words.sort()
    words = list(dict.fromkeys(words)) #remove duplicates
    
    #translate and print
    translator = Translator()
    translations = translator.translate(words, src=source_lang, dest=dest_lang)
    for translation in translations:
        print(translation.origin , " , " , translation.text)
    
    #clean up
    file.close()

if __name__ == '__main__':
    parse_json_and_print_translations(PATH_TO_JSON_FILE)
