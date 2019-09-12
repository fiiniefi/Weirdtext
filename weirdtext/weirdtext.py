import re
import random


def encode(text):
    """
    Encodes text using Weirdtext algorithm

    :param str text: Text to encode
    :rtype: Tuple[str, list]
    :return: pair (encoded_text, sorted_input_words)
    """
    words = get_words_with_delimiters(text)
    encoded_words = get_coded_words(words, encode_word)
    return "".join(encoded_words), sorted(re.split(r'\W+', text), key=str.lower)


def decode(text, original_words):
    """
    Decodes text encoded by Weirdtext algorithm

    :param str text: Text to decode
    :param list original_words: list of decoded words
    :rtype: str
    :return: decoded text
    """
    words = get_words_with_delimiters(text)
    decoded_words = get_coded_words(words, decode_word, original_words)
    return "".join(decoded_words)


def encode_word(word):
    if len(word) < 4 or consists_of_one_unique_letter(word[1:-1]):
        return word
    return next(encoded for encoded in randomize_word(word) if encoded is not None)


def randomize_word(word):
    #  non-deterministic
    letters = list(word[1:-1])
    while True:
        random.shuffle(letters)
        encoded = "".join(letters)
        yield word.replace(word[1:-1], encoded) if encoded != word[1:-1] else None


def decode_word(word, original_words):
    for pattern in original_words:
        if sorted(word) == sorted(pattern):
            return pattern


def get_words_with_delimiters(text):
    return re.split(r'(\W+)', text)


def get_coded_words(words, codec, *args):
    for word in words:
        yield codec(word, *args) if word.isalpha() else word


def consists_of_one_unique_letter(word):
    return len(set(word)) == 1
