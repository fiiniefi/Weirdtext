import re
import random


def encode(text):
    words = get_words_with_delimiters(text)
    encoded_words = get_coded_words(words, encode_word)
    return "".join(encoded_words), sorted(re.split('\\W+', text), key=str.lower)


def decode(text, array):
    words = get_words_with_delimiters(text)
    decoded_words = get_coded_words(words, decode_word, array)
    return "".join(decoded_words)


def encode_word(word):
    if len(word) < 4 or has_one_unique_letter(word[1:-1]):
        return word
    while True:
        letters = list(word[1:-1])
        random.shuffle(letters)
        encoded = "".join(letters)

        if encoded != word[1:-1]:
            return word.replace(word[1:-1], encoded)


def decode_word(word, array):
    for pattern in array:
        if sorted(word) == sorted(pattern):
            return pattern


def get_words_with_delimiters(text):
    return re.split('(\\W+)', text)


def get_coded_words(words, coder, *args):
    return [coder(word, *args) if word.isalpha() else word
            for word in words]


def has_one_unique_letter(word):
    return len(list(dict.fromkeys(word))) == 1