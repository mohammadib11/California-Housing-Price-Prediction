import pickle as pkl

def LoadModel(file_path : str) :
    with open(file_path, 'rb') as file :
        loaded_model = pkl.load(file)
    return loaded_model