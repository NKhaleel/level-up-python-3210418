import re


def is_palindrome(words):
    extract = re.sub('[^a-zA-Z]', '', words)

    final_extract = extract.lower()

    if (final_extract == final_extract[::-1]):
        return True
    else:
        return False
