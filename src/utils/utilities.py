import pickle
import os

def save_object(object,filename):
    cwd = os.getcwd()
    location = os.path.join(cwd,'artifacts')
    os.makedirs(location,exist_ok=True)
    file_loc = os.path.join(location, filename + '.pkl')
    with open(file_loc, 'wb') as f:
        pickle.dump(object, f)
    return  file_loc    



def load_object(filename):
    cwd = os.getcwd()
    location = os.path.join(cwd,'artifacts')
    os.makedirs(location,exist_ok=True)
    file_loc = os.path.join(location, filename)
    with open(file_loc, 'rb') as f:
        return pickle.load(f)



