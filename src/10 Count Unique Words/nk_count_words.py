from collections import Counter


def count_words(file_path):

    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.read()

    ulines = lines.upper()
    count = Counter(ulines.split())
    # unique = set(text.split())

    print("Total Number of Unique Words: \n" + str(len(count)))

    print("Top 20 Words:")
    for c in count.most_common(20):
        print(c)

    f.close()
