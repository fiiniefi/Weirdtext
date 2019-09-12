import pytest
from weirdtext.weirdtext import encode, decode


@pytest.mark.parametrize('input_text', ('  \nThis  is a sample text \n',
                                        open('../resources/text1').read(),
                                        ),
                         )
def test_EncodeDecode_CodesCorrectly(input_text):
    print(input_text)
    encoded_text, words = encode(input_text)
    decoded_text = decode(encoded_text, words)
    assert decoded_text == input_text
