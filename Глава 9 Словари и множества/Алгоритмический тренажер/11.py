import pickle

set1 = {1, 2, 3, 4, 5, 6}


def pickle_objects():
    with open('mydata.dat', 'wb') as output_file:
        pickle.dump(set1, output_file)


pickle_objects()
