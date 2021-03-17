"""
Module that search for English digits
in a string and replace it with Arabic digits

@dependencies:
pip install arabic_reshaper
pip install python-bidi

@author
Ahmed salama
"""


def ar_txt(text):
    from arabic_reshaper import reshape
    from bidi.algorithm import get_display
    """
    correct text's Shape using arabic_reshaper, And Its Direction using Python-bidi
    :param text: The Text to be fixed
    :return: Fixed Text
    """
    reshaped_text = reshape(text)
    return get_display(reshaped_text)


def sentence_with_ar_digits(s):
    s = ar_txt(str(s))
    numeral_map = ['٠', '١', '٢', '٣', '٤', '٥', '٦', '٧', '٨', '٩']
    s = s.replace('0', numeral_map[0])
    s = s.replace('1', numeral_map[1])
    s = s.replace('2', numeral_map[2])
    s = s.replace('3', numeral_map[3])
    s = s.replace('4', numeral_map[4])
    s = s.replace('5', numeral_map[5])
    s = s.replace('6', numeral_map[6])
    s = s.replace('7', numeral_map[7])
    s = s.replace('8', numeral_map[8])
    s = s.replace('9', numeral_map[9])
    return s


def run():
    sentence = "Hello world, My name is Ahmed i'm 24 years old. Born in 1996."
    sentence_with_arabic_numbers = sentence_with_ar_digits(sentence)
    print(sentence_with_arabic_numbers)


if __name__ == "__main__":
    run()
