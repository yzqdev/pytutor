import pickle

pickle_file = open("..\dist\my_list.pkl", "rb")
my_list = pickle.load(pickle_file)
print(my_list)
