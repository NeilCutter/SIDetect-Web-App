from webapp import pickle


def load_model(filename):
    with open(filename, "rb") as infile:
        return pickle.load(infile)


def load_file(filename):
    with open(filename, "r", encoding="utf-8") as infile:
        return infile.read()

