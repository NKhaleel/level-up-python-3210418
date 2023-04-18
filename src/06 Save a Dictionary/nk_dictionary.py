import pickle


def save_dict(dict_in, file_name):
    with open(file_name, "wb") as f:
        pickle.dump(dict_in, f)


def load_dict(file_name):
    with open(file_name, "rb") as f:
        return pickle.load(f)
