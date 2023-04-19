import secrets


def generate_passphrase(words, wordlist_path="diceware.wordlist.asc"):
    with open(wordlist_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()[2:7778]
        num_list = [line.split()[0] for line in lines]
        word_list = [line.split()[1] for line in lines]

    search = []
    words_all = []

    for i in range(words):
        search.append("".join(str(e)
                      for e in secrets.choices(range(1, 6), k=5)))

    for code in search:
        words_all.append(word_list[num_list.index(code)])

    return " ".join(words_all)
