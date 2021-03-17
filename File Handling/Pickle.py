import pickle


def store():
    dict_data = {"Name": "Vijay", "Age": "20", "Gender": "Male"}
    file = open(
        "Pickle.pkl", "wb"
    )  # For pickle files use WB - Write and read from a binary file.
    pickle.dump(dict_data, file)
    file.close()


def load():
    with open("assets/Pickle.pkl", "rb") as fp:
        data = pickle.load(fp)
    print(data)


if __name__ == "__main__":
    store()
    load()
