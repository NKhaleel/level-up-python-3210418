def sort_words(text):

    all_words = text.split()
    all_words.sort(key=str.casefold)
    " ".join(all_words)

    return all_words
