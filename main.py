source_lang = 'es'
dest_lang = 'en'

method = "API" #API or JSON
duolingo_user = "MarkFobert"
duolingo_pass = "some_fake_password"
PATH_TO_JSON_FILE = '/home/mark/Downloads/overview.json' #JSON FILE FROM https://www.duolingo.com/vocabulary/overview  (JSON tab -> Save)

import json
from googletrans import Translator #pip install googletrans
import duolingo #pip install duolingo-api


def print_translations(translations):
    for k, v in translations.items():
        print(v, ": ", k)


def get_translations(words, source_lang, dest_lang):
    translator = Translator()
    translations = translator.translate(words, src=source_lang, dest=dest_lang)
    translation_dict = {}
    for translation in translations:
        translation_dict[translation.text] = translation.origin
    return translation_dict


def get_words_from_API(username, password, lang):
    lingo = duolingo.Duolingo(username, password)
    vocab = lingo.get_vocabulary(language_abbr=lang)['vocab_overview']
    words = []
    for word_json_object in vocab:
        words.append(word_json_object['word_string'])
    words.sort()
    words = list(dict.fromkeys(words))  # remove duplicates
    return words

def get_words_from_JSON(filename):
    # open and parse
    file = open(filename, "r")
    json_contents = file.read()
    json_parsed = json.loads(json_contents)
    word_json_objects = json_parsed['vocab_overview']
    words = []
    for word_json_object in word_json_objects:
        words.append(word_json_object['word_string'])
    # sort and filter
    words.sort()
    words = list(dict.fromkeys(words))  # remove duplicates
    file.close()
    return words

if __name__ == '__main__':
    words = []
    if method == "API":
        words = get_words_from_API(duolingo_user, duolingo_pass, source_lang)
    elif method == "JSON":
        words = get_words_from_JSON(PATH_TO_JSON_FILE)
    translations = get_translations(words, source_lang, dest_lang)
    print_translations(translations)