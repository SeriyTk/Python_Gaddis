import pickle


def unpickle_objects():
    with open('mydata.dat', 'rb') as input_file:
        set1 = pickle.load(input_file)
    print(set1)


unpickle_objects()
