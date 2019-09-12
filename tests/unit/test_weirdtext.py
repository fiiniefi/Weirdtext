import pytest
from mock import Mock, ANY
import weirdtext
from weirdtext.weirdtext import encode, decode, encode_word, decode_word


@pytest.fixture
def code_mock(monkeypatch):
    monkeypatch.setattr(weirdtext.weirdtext, 'get_words_from_text', Mock(['dsa', 'asd']))
    monkeypatch.setattr(weirdtext.weirdtext, 'get_coded_words', Mock(return_value=['asd', 'dsa']))


def test_Decode_ReturnsValidOutput(code_mock):
    assert decode(ANY, ANY) == 'asddsa'


def test_Encode_ReturnsValidOutput(code_mock):
    assert encode('text sample') == ('asddsa', ['sample', 'text'])


def test_EncodeWord_ReturnsShortWordUntouched(monkeypatch):
    monkeypatch.setattr(weirdtext.weirdtext, 'random', Mock())
    word = 'asd'
    assert word == encode_word(word)


@pytest.mark.parametrize('word', ('word', 'module', 'function', 'name', 'interface', 'python'))
def test_EncodeWord_ShufflesWordCorrectly(monkeypatch, word):
    monkeypatch.setattr(weirdtext.weirdtext, 'has_one_unique_letter', Mock(return_value=False))
    assert word != encode_word(word)


@pytest.mark.parametrize('word, array', [('wrod', ['word']),
                                         ('mudloe', ['module']),
                                         ('fcuntoin', ['function']),
                                         ('nmae', ['name']),
                                         ],
                         )
def test_DecodeWord_UncodesWordCorrectly(word, array):
    assert array[0] == decode_word(word, array)


@pytest.mark.parametrize('word, array', [('wrod', ['wordd']),
                                         ('mudloe', ['modle']),
                                         ('fcuntoin', ['funcrion']),
                                         ('nmae', ['nane']),
                                         ],
                         )
def test_DecodeWord_ValidPatternNotProvided(word, array):
    assert decode_word(word, array) is None
